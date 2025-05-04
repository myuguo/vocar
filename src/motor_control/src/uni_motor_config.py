#!/usr/bin/env python3

import rospy
from dynamic_reconfigure.server import Server
from motor_control.cfg import MotorConfigurationConfig
from chip_bldc_driver.msg import Config, Command, Feedback  # Import Feedback message too

class MotorConfigurator:
    def __init__(self):
        rospy.init_node('motor_configurator')

        # Publishers
        self.pub = rospy.Publisher('/bldc_driver_node/Config', Config, queue_size=10)
        self.pub_cmd = rospy.Publisher('/bldc_driver_node/Command', Command, queue_size=10)

        # Subscribers
        self.sub_feedback = rospy.Subscriber('/bldc_driver_node/feedback', Feedback, self.feedback_callback)

        # Dynamic reconfigure server
        self.last_config = None
        self.srv = Server(MotorConfigurationConfig, self.reconfigure_callback)

        # Initialize motor speed and feedback
        self.motor_speed_value = 0
        self.last_encoder_count = None
        self.last_feedback_time = None

        # Constants
        self.counts_per_revolution = 90    # You measured 90 counts per mechanical wheel revolution
        self.wheel_radius_m = 0.1           # 100 mm -> 0.1 meters
        self.wheel_circumference_m = 2 * 3.14159265359 * self.wheel_radius_m

        # Timer for constant speed publishing (e.g., 10Hz)
        publish_rate = 10
        self.timer = rospy.Timer(rospy.Duration(1.0 / publish_rate), self.timer_callback)

        rospy.loginfo("[MotorConfigurator] Node started with speed publish rate = %d Hz.", publish_rate)

        rospy.spin()

    def reconfigure_callback(self, config, level):
        rospy.loginfo("[MotorConfigurator] Dynamic Reconfigure Callback triggered.")

        if self.last_config is None:
            self.last_config = config
            self.motor_speed_value = config.MC
            return config

        # Compare each parameter
        self.compare_and_send("MM",    self.last_config.MM,    config.MM)
        self.compare_and_send("MAMP",  self.last_config.MAMP,  config.MAMP)
        self.compare_and_send("MKP",   self.last_config.MKP,   config.MKP)
        self.compare_and_send("MKI",   self.last_config.MKI,   config.MKI)
        self.compare_and_send("MKD",   self.last_config.MKD,   config.MKD)
        self.compare_and_send("MMRPM", self.last_config.MMRPM, config.MMRPM)
        self.compare_and_send("MPP",   self.last_config.MPP,   config.MPP)
        self.compare_and_send("MBK",   self.last_config.MBK,   config.MBK)
        self.compare_and_send("MWT",   self.last_config.MWT,   config.MWT)
        self.compare_and_send("MPEC",  self.last_config.MPEC,  config.MPEC)

        self.motor_speed_value = config.MC
        self.last_config = config
        return config

    def compare_and_send(self, param_code, old_value, new_value):
        if old_value != new_value:
            msg = Config()
            msg.param_code = param_code
            msg.param_value = new_value
            self.pub.publish(msg)
            rospy.loginfo("[MotorConfigurator] Sent Config: %s = %d", param_code, new_value)

    def timer_callback(self, event):
        cmd = Command()

        # Convert m/s to RPM (must be int)
        rpm_command = int(self.motor_speed_value * 60 / (2 * 3.14159265359 * 0.1))
        cmd.motor_command = rpm_command

        self.pub_cmd.publish(cmd)
        rospy.logdebug("[MotorConfigurator] Sent Motor Speed Command: %.2f m/s → %d RPM", self.motor_speed_value, rpm_command)


    def feedback_callback(self, msg):
        encoder_count = msg.motor_encoder_counter
        current_time = rospy.Time.now()
        interval = 0.25  # Only calculate every 200 ms

        # --- Print odometry (always) ---
        wheel_rotations = encoder_count / float(self.counts_per_revolution)
        odom_m = wheel_rotations * self.wheel_circumference_m

        # --- Calculate speed (every 0.2s) ---
        if self.last_encoder_count is not None and self.last_feedback_time is not None:
            delta_time = (current_time - self.last_feedback_time).to_sec()

            if delta_time >= interval:
                delta_counts = encoder_count - self.last_encoder_count

                # Calculate speed in m/s from encoder delta
                rotations = delta_counts / float(self.counts_per_revolution)
                linear_speed_from_encoder = (rotations * self.wheel_circumference_m) / delta_time

                # Calculate mechanical RPM from encoder delta
                rps = rotations / delta_time
                rpm_from_encoder = rps * 60

                if rpm_from_encoder != 0:
                    rospy.loginfo("[MotorConfigurator] From Encoder: %.2f m/s, %.2f RPM", linear_speed_from_encoder, rpm_from_encoder)

                # Update only if we actually computed
                self.last_encoder_count = encoder_count
                self.last_feedback_time = current_time
        else:
            # First-time init
            self.last_encoder_count = encoder_count
            self.last_feedback_time = current_time



if __name__ == '__main__':
    MotorConfigurator()
