#!/bin/python3
from os import CLD_DUMPED
from turtle import pu
import os,sys
sys.path.append("/home/mox/test_urdf_tool_ws/src/automony/automony")
import pub_turtle,kill,client_spwan,rclpy,random_Target

global CL
def mainSpawn (args=None):
    global CL
    CL = client_spwan.client_spwan()
    rclpy.spin_once(CL)
    # CL.destroy_node()
    # target_turtle_node = random_Target.TargetTurtleNode()
    # rclpy.spin_once(target_turtle_node)
    # target_turtle_node.destroy_node()

def mainPub (args=None):
    node=pub_turtle.MyNode()
    while node.finished == False :
        rclpy.spin_once(node)
    # node.destroy_node()
    
def mainKill (x,y,args=None):
    node1=kill.my_server()
    rclpy.spin_once(node1)
    # node1.destroy_node()

def main (args=None):
    global CL
    while True:
        rclpy.init(args=args)
        mainSpawn()
        mainPub()
        mainKill(CL.x,CL.y)
        rclpy.shutdown()
