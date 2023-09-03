#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.srv import Kill

class my_server(Node):
    def __init__(self):
        super().__init__("Client_OOP_node")
        self.client=self.create_client(Kill,"/kill")
        self.Kill_services("Target_turtle")
        

    def Kill_services(self,turtle_name):
        print(turtle_name)
        if not (self.client.wait_for_service(1)):
            self.get_logger().warn("wating for server")
            print("Wating ",end="")
            while not (self.client.wait_for_service(1)):
                print(".",end="")
        
        print("\m Connected")
        request= Kill.Request()
        request.name=turtle_name
        turtle=self.client.call_async(request)



def main (args=None):
    rclpy.init(args=args)
    node1=my_server()
    rclpy.spin_once(node1)
    rclpy.shutdown()
