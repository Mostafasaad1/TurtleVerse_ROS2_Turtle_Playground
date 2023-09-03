#!/usr/bin/env python3
import rclpy
from random import randint, uniform 
from rclpy.node import Node
from turtlesim.srv import Spawn
from string import ascii_uppercase

class client_spwan(Node):
    def __init__(self):
        super().__init__("Client_OOP_node")
        self.client=self.create_client(Spawn,"/spawn") 
        
        x = round(uniform(1,10),1)
        y = round(uniform(1,10),1)
        name = "Target_turtle" #"Turtle" + ascii_uppercase[randint(0,len(ascii_uppercase))]
        self.x=x
        self.y=y
        self.Spawn_new(x,y,1.5,str(name))
        

    def Spawn_new(self,x,y,theta,turtle_name):
        
        while self.client.wait_for_service(1)==False:
            self.get_logger().warn("wating for server")

        request=Spawn.Request()
        request.x=x
        request.y=y
        request.theta=theta
        request.name=turtle_name
        
        futur_obj=self.client.call_async(request)

        futur_obj.add_done_callback(self.CallBack)

    def CallBack(self,future_msg):    
            print(f"response is, {future_msg.result().name}")

       


def main (args=None):
    rclpy.init(args=args)
    rclpy.spin_once(node1)
    rclpy.shutdown()

