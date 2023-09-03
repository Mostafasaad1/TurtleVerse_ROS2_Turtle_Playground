import rclpy
from rclpy.node import Node
from math import pow, atan2, sqrt, pi
from geometry_msgs.msg import Twist, Pose2D
from turtlesim.msg import Pose

class MyNode(Node):
    def __init__(self):
        super().__init__("go_to_goal_x_y")
        print("Initializing")
        self.goToWaypoint = True
        self.current = Pose2D()
        self.target_pose = Pose()
        self.waypointGoal = Pose2D()
        self.waypointGoal.x = 0.0
        self.waypointGoal.y = 0.0
        self.velCommand = Twist()
        self.velCommand.linear.x = 0.0
        self.velCommand.angular.z = 0.0
        self.K_l = 2
        self.K_a = 3
        self.distanceTolerance = 0.2
        self.angleTolerance = 0.01
        self.finished = False
        self.seeker_pose_subscriber = self.create_subscription(Pose, "/turtle1/pose", self.updatePose, 10)
        self.velocity_publisher = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.target_pose_subscriber = self.create_subscription(Pose, '/Target_turtle/pose', self.updateTargetPose, 10)


    def updateTargetPose(self, msg):
        self.waypointGoal.x = float(msg.x)
        self.waypointGoal.y = float(msg.y)
        # print(msg.x,msg.y,msg.theta)

        # self.target_pose = msg

    def updatePose(self, data):
        self.current.x = round(data.x, 5)
        self.current.y = round(data.y, 5)
        self.current.theta = data.theta
        # print(self.current.x, self.current.y, self.current.theta)

        # Calculate distance and angle to the goal waypoint
        distance = abs(sqrt(pow(self.waypointGoal.x - self.current.x, 2) + pow(self.waypointGoal.y - self.current.y, 2)))
        angle = atan2(self.waypointGoal.y - self.current.y, self.waypointGoal.x - self.current.x)

        # Check if the goal has been reached
        if distance <= self.distanceTolerance:
            self.finished = True
            self.stopRobot()
            print("Goal reached!")
            # # exit()
            # rclpy.shutdown() 
            # return

        # Rotate towards the goal
        self.rotateTowardsGoal(angle)

        # Move towards the goal
        self.moveTowardsGoal(distance)

    def rotateTowardsGoal(self, angle):
        angular_error = angle - self.current.theta
        while angular_error > pi:
            angular_error -= 2 * pi
        while angular_error < -pi:
            angular_error += 2 * pi

        # self.velCommand.linear.x = 0.0
        self.velCommand.angular.z = self.K_a * angular_error
        self.publishVelocity()

    def moveTowardsGoal(self, distance):
        linear_error = distance
        self.velCommand.linear.x = self.K_l * linear_error
        # self.velCommand.angular.z = 0.0
        self.publishVelocity()

    def publishVelocity(self):
        self.velocity_publisher.publish(self.velCommand)

    def stopRobot(self):
        self.velCommand.linear.x = 0.0
        self.velCommand.angular.z = 0.0
        self.publishVelocity()


# def main(x, y):
#     rclpy.init()
#     node = MyNode(x, y)
#     rclpy.spin(node)
#     node.destroy_node()
#     rclpy.shutdown()

'''

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Pose
from turtlesim.msg import Pose as TurtlePose

class FollowTargetNode(Node):
    def __init__(self):
        super().__init__('follow_target_node')
        self.finished = False
        self.target_pose = TurtlePose()
        self.my_pose = TurtlePose()
        self.velocity_publisher = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.target_pose_subscriber = self.create_subscription(TurtlePose, 'target_turtle/pose', self.updateTargetPose, 10)
        self.my_pose_subscriber = self.create_subscription(TurtlePose, 'turtle1/pose', self.updateMyPose, 10)
        self.timer = self.create_timer(0.1, self.followTarget)

    def updateTargetPose(self, msg):
        self.target_pose = msg

    def updateMyPose(self, msg):
        self.my_pose = msg

    def followTarget(self):
        distance = self.calculateDistance()
        angle = self.calculateAngle()
        while angle > pi:
            angle -= 2 * pi
        while angle < -pi:
            angle += 2 * pi

        twist_msg = Twist()
        twist_msg.linear.x = 0.9 * distance
        twist_msg.angular.z = 3 * angle
        self.velocity_publisher.publish(twist_msg)
        if distance < 0.01 : 
            self.finished=True
            print("Goal")

            


    def calculateDistance(self):
        return  abs(sqrt(pow(self.target_pose.x - self.my_pose.x, 2) + pow(self.target_pose.y - self.my_pose.y, 2)))

    def calculateAngle(self):
        return atan2(self.target_pose.y - self.my_pose.y, self.target_pose.x - self.my_pose.x)


def main():
    rclpy.init()
    follow_target_node = FollowTargetNode()
    rclpy.spin(follow_target_node)
    follow_target_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
    '''