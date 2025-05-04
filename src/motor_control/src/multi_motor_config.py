#!/usr/bin/env python3

import rospy
from dynamic_reconfigure.server import Server
from motor_control.cfg import MotorConfigurationConfig
from chip_bldc_driver.msg import Config, Command, Feedback

class MotorSide:
    def __init__(self, side_name, namespace, wheel_radius_m=0.1, counts_per_rev=90):
        self.side_name = side_name
        self.ns = namespace

        self.config_pub = rospy.Publisher(f"{self.ns}/bldc_driver_node/Config", Config, queue_size=10)
        self.cmd_pub = rospy.Publisher(f"{self.ns}/bldc_driver_node/Command", Command, queue_size=10)
        self.feedback_sub = rospy.Subscriber(f"{self.ns}/bldc_driver_node/feedback", Feedback, self.feedback_callback)

        self.motor_speed_mps = 0.0
        self.last_encoder_count = None
        self.last_feedback_time = None

        self.counts_per_rev = counts_per_rev
        self.wheel_radius = wheel_radius_m
        self.wheel_circumference = 2 * 3.14159265359 * wheel_radius_m

    def send_config(self, param_code, value):
        msg = Config()
        msg.param_code = param_code
        msg.param_value = value
        self.config_pub.publish(msg)
        rospy.loginfo(f"[{self.side_name}] Sent Config: {param_code} = {value}")

    def send_speed_command(self):
        rpm = int(self.motor_speed_mps * 60 / self.wheel_circumference)
        cmd = Command()
        cmd.motor_command = rpm
        self.cmd_pub.publish(cmd)
        rospy.logdebug(f"[{self.side_name}] Sent Speed Command: {self.motor_speed_mps:.2f} m/s → {rpm} RPM")

    def feedback_callback(self, msg):
        encoder_count = msg.motor_encoder_counter
        current_time = rospy.Time.now()
        interval = 0.2

        # Odom from total encoder
        wheel_rotations = encoder_count / float(self.counts_per_rev)
        odom_m = wheel_rotations * self.wheel_circumference
        rospy.loginfo(f"[{self.side_name}] Odom: {odom_m:.3f} m (Encoder: {encoder_count})")

        if self.last_encoder_count is not None and self.last_feedback_time is not None:
            delta_time = (current_time - self.last_feedback_time).to_sec()
            if delta_time >= interval:
                delta_counts = encoder_count - self.last_encoder_count
                rotations = delta_counts / float(self.counts_per_rev)
                linear_speed = (rotations * self.wheel_circumference) / delta_time
                rospy.loginfo(f"[{self.side_name}] Speed: {linear_speed:.2f} m/s")

                self.last_encoder_count = encoder_count
                self.last_feedback_time = current_time
        else:
            self.last_encoder_count = encoder_count
            self.last_feedback_time = current_time


class DualMotorConfigurator:
    def __init__(self):
        rospy.init_node("dual_motor_configurator")

        self.left = MotorSide("Left", "/left_motor")
        self.right = MotorSide("Right", "/right_motor")

        self.last_config = None
        self.srv = Server(MotorConfigurationConfig, self.reconfigure_callback)

        self.timer = rospy.Timer(rospy.Duration(0.1), self.timer_callback)
        rospy.loginfo("[DualMotorConfigurator] Started.")

        rospy.spin()

    def reconfigure_callback(self, config, level):
        rospy.loginfo("[Reconfigure] Callback triggered.")

        if self.last_config is None:
            self.last_config = config
            self.left.motor_speed_mps = config.MC
            self.right.motor_speed_mps = config.MC
            return config

        for param_code in ["MM", "MAMP", "MKP", "MKI", "MKD", "MMRPM", "MPP", "MBK", "MWT", "MPEC"]:
            old = getattr(self.last_config, param_code)
            new = getattr(config, param_code)
            if old != new:
                self.left.send_config(param_code, new)
                self.right.send_config(param_code, new)

        self.left.motor_speed_mps = config.MC
        self.right.motor_speed_mps = config.MC
        self.last_config = config
        return config

    def timer_callback(self, event):
        self.left.send_speed_command()
        self.right.send_speed_command()


if __name__ == "__main__":
    DualMotorConfigurator()
