#!/usr/bin/env python

__author__ = "monoDrive"
__copyright__ = "Copyright (C) 2018 monoDrive"
__license__ = "MIT"
__version__ = "1.0"

# Copyright (c) 2017 Computer Vision Center (CVC) at the Universitat Autonoma de
# Barcelona (UAB), and the INTEL Visual Computing Lab.
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.



"""
Class to handle control input
"""

import math
import numpy as np
import rospy

from ackermann_msgs.msg import AckermannDrive


class InputController(object):
    """
    Class to handle monodrive_ros_bridge input command

    Each time a monodrive_ros_bridge control msg (an ackermann_cmd msg) is received on control topic, a mono control message is
    computed.
    """

    def __init__(self, topic_name='/ackermann_cmd'):
        # current control command
        self.cur_control = {
            'steer': 0.0,
            'throttle': 0.0,
            'brake': 0.0,
            'hand_brake': False,
            'reverse': False
        }

        self.cmd_vel_subscriber = rospy.Subscriber(
            '/ackermann_cmd', AckermannDrive, self.set_control_cmd_callback)

    def set_control_cmd_callback(self, data):
        """
        Convert a Ackerman drive msg into mono control msg

        Right now the control is really simple and don't enforce acceleration and jerk command, nor the steering acceleration too
        :param data: AckermannDrive msg
        :return:
        """
        steering_angle_ctrl = data.steering_angle
        speed_ctrl = data.speed

        max_steering_angle = math.radians(
            500
        )  # 500 degrees is the max steering angle that I have on my car,
        #  would be nice if we could use the value provided by mono
        max_speed = 27  # just a value for me, 27 m/sec seems to be a reasonable max speed for now

        control = {}

        if abs(steering_angle_ctrl) > max_steering_angle:
            rospy.logerr("Max steering angle reached, clipping value")
            steering_angle_ctrl = np.clip(
                steering_angle_ctrl, -max_steering_angle, max_steering_angle)

        if abs(speed_ctrl) > max_speed:
            rospy.logerr("Max speed reached, clipping value")
            speed_ctrl = np.clip(speed_ctrl, -max_speed, max_speed)

        if speed_ctrl == 0:
            control['brake'] = True

        control['steer'] = steering_angle_ctrl / max_steering_angle
        control['throttle'] = abs(speed_ctrl / max_speed)
        control['reverse'] = True if speed_ctrl < 0 else False

        self.cur_control = control
