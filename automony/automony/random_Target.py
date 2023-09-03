#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import random

class TargetTurtleNode(Node):
    def __init__(self):
        super().__init__('target_turtle_node')
        self.publisher_ = self.create_publisher(Twist, 'Target_turtle/cmd_vel', 10)
        self.timer_ = self.create_timer(1.0, self.publish_random_values)

    def publish_random_values(self):
        twist_msg = Twist()
        twist_msg.linear.x = random.uniform(-10, 10)  # Set a random linear velocity between 0 and 10
        twist_msg.angular.z = random.uniform(-2, 2)  # Set a random angular velocity between 0 and 2
        # print(twist_msg.linear.x)
        self.publisher_.publish(twist_msg)
        self.get_logger().info("Published random values")

def main(args=None):
    rclpy.init(args=args)
    target_turtle_node = TargetTurtleNode()
    rclpy.spin(target_turtle_node)
    target_turtle_node.destroy_node()
    rclpy.shutdown()
