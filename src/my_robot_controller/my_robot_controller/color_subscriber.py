#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Color


class ColorubscriberNode(Node):

    def __init__(self):
        super().__init__("color_subscriber")
        self.color_subscriber_ = self.create_subscription(
            Color, "/turtle1/color_sensor", self.color_callback, 10)

    def color_callback(self, msg):
        self.get_logger().info(str(msg))


def main(args=None):
    rclpy.init(args=args)
    node = ColorubscriberNode()
    rclpy.spin(node)

    rclpy.shutdown
