# TurtleVerse_ROS2_Turtle_Playground
ROS2 Turtle Control System is a simulation-based project that leverages the power of ROS2 to control and interact with virtual turtles in a dynamic environment. This project offers a comprehensive suite of functionalities, including spawning and controlling turtles, following target turtles, and performing turtle termination


## System 
* Ubuntu Jammy 22 
* ROS2 Humble 

## How to install it 
```
$ cd /path/to/your/ros2_workspace/src
$ git clone https://github.com/Mostafasaad1/TurtleVerse_ROS2_Turtle_Playground.git -b automony
```
in file automony/automony/catch.py
you have to add your workspace path 
```
sys.path.append("/<Workspace_Absoulte_path>/src/automony/automony")
```
then 
```
$ colcon build --packages-select automony --symlink-install
```
## how to run it 
if needed source your workspace 
in Terminal 1 
```
ros2 run turtlesim turtlesim_node
```
in Terminal 2
```
ros2 run automony catch
```
in Terminal 3 ( To make the target Turtle move)
```
ros2 run automony random_Terget
```
