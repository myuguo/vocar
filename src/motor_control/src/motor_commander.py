#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Quaternion
from tf.transformations import quaternion_from_euler
import tf
from chip_bldc_driver.msg import Command, Feedback
import math


class EncoderWheel:
    def __init__(self, counts_per_rev, wheel_circumference):
        self.counts_per_rev = counts_per_rev
        self.wheel_circumference = wheel_circumference
        self.last_encoder_count = None
        self.last_time = None
        self.linear_speed_mps = 0.0


class DiffDriveNode:
    def __init__(self):
        rospy.init_node("diff_drive_node")

        # Robot parameters
        self.wheel_radius = rospy.get_param("~wheel_radius", 0.1)
        self.wheel_base = rospy.get_param("~wheel_base", 0.4)
        self.counts_per_rev = rospy.get_param("~counts_per_rev", 90)
        self.fencoder = rospy.get_param("~fencoder", 5)
        self.fodom = rospy.get_param("~fodom", 10)

        self.wheel_circumference = 2 * 3.14159265359 * self.wheel_radius
        self.encoder_interval = 1 / self.fencoder

        # Wheels
        self.left_wheel = EncoderWheel(self.counts_per_rev, self.wheel_circumference)
        self.right_wheel = EncoderWheel(self.counts_per_rev, self.wheel_circumference)

        # Pose
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0
        self.last_integration_time = rospy.Time.now()

        # Publishers
        self.left_cmd_pub = rospy.Publisher("/left_motor/bldc_driver_node/Command", Command, queue_size=10)
        self.right_cmd_pub = rospy.Publisher("/right_motor/bldc_driver_node/Command", Command, queue_size=10)
        self.odom_pub = rospy.Publisher("/odom", Odometry, queue_size=10)
        self.tf_broadcaster = tf.TransformBroadcaster()

        # Subscribers
        self.last_cmd_vel = Twist()
        rospy.Subscriber("/cmd_vel", Twist, self.cmd_vel_callback)
        rospy.Subscriber("/left_motor/bldc_driver_node/feedback", Feedback, self.left_feedback_callback)
        rospy.Subscriber("/right_motor/bldc_driver_node/feedback", Feedback, self.right_feedback_callback)

        # Timer for odometry update
        odom_interval = 1 / self.fodom
        self.odom_timer = rospy.Timer(rospy.Duration(odom_interval), self.integrate_odometry)

        # Timer to regularly publish motor commands
        self.cmd_timer = rospy.Timer(rospy.Duration(0.1), self.publish_motor_commands)  # 10 Hz

        rospy.loginfo("[DiffDriveNode] Node initialized.")
        rospy.spin()

    def cmd_vel_callback(self, msg):
        self.last_cmd_vel = msg

    def publish_motor_commands(self, event):
        v = self.last_cmd_vel.linear.x
        omega = self.last_cmd_vel.angular.z

        if omega == 0:
            v_left = v
            v_right = v
        else:
            v_left = v - (omega * self.wheel_base / 2.0)
            v_right = v + (omega * self.wheel_base / 2.0)

        left_cmd = Command()
        right_cmd = Command()
        left_cmd.motor_command = int((v_left * 60.0) / self.wheel_circumference)
        right_cmd.motor_command = int((v_right * 60.0) / self.wheel_circumference)

        self.left_cmd_pub.publish(left_cmd)
        self.right_cmd_pub.publish(right_cmd)

        rospy.loginfo_throttle(1.0, "[cmd_vel] v=%.2f ω=%.2f → L=%.2f, R=%.2f → %d, %d",
                            v, omega, v_left, v_right, left_cmd.motor_command, right_cmd.motor_command)



    def left_feedback_callback(self, msg):
        self.process_encoder_feedback(msg.motor_encoder_counter, self.left_wheel, self.encoder_interval)

    def right_feedback_callback(self, msg):
        self.process_encoder_feedback(msg.motor_encoder_counter, self.right_wheel, self.encoder_interval)

    def process_encoder_feedback(self, encoder_count, wheel, interval=0.25):
        current_time = rospy.Time.now()

        if wheel.last_encoder_count is not None and wheel.last_time is not None:
            delta_time = (current_time - wheel.last_time).to_sec()
            if delta_time >= interval:
                delta_counts = encoder_count - wheel.last_encoder_count
                rotations = delta_counts / float(wheel.counts_per_rev)
                wheel.linear_speed_mps = (rotations * wheel.wheel_circumference) / delta_time

                wheel.last_encoder_count = encoder_count
                wheel.last_time = current_time
        else:
            wheel.last_encoder_count = encoder_count
            wheel.last_time = current_time

    def integrate_odometry(self, event):
        now = rospy.Time.now()
        dt = (now - self.last_integration_time).to_sec()
        self.last_integration_time = now

        v_left = self.left_wheel.linear_speed_mps
        v_right = self.right_wheel.linear_speed_mps

        v = (v_right + v_left) / 2.0
        omega = (v_right - v_left) / self.wheel_base

        delta_x = v * dt * math.cos(self.theta)
        delta_y = v * dt * math.sin(self.theta)
        delta_theta = omega * dt

        self.x += delta_x
        self.y += delta_y
        self.theta += delta_theta

        quat = quaternion_from_euler(0, 0, self.theta)
        odom = Odometry()
        odom.header.stamp = now
        odom.header.frame_id = "odom"
        odom.child_frame_id = "base_link"

        odom.pose.pose.position.x = self.x
        odom.pose.pose.position.y = self.y
        odom.pose.pose.orientation = Quaternion(*quat)
        odom.twist.twist.linear.x = v
        odom.twist.twist.angular.z = omega

        self.odom_pub.publish(odom)

        self.tf_broadcaster.sendTransform(
            (self.x, self.y, 0.0),
            quat,
            now,
            "base_link",
            "odom"
        )

        rospy.loginfo("[Odom] x=%.2f y=%.2f θ=%.2f | v=%.2f m/s ω=%.2f rad/s",
                      self.x, self.y, self.theta, v, omega)


if __name__ == "__main__":
    try:
        DiffDriveNode()
    except rospy.ROSInterruptException:
        pass
