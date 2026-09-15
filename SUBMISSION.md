# Lab 1: Intro to ROS 2

## Written Questions

### Q1: During this assignment, you've probably ran these two following commands at some point: ```source /opt/ros/humble/setup.bash``` and ```source install/local_setup.bash```. Functionally what is the difference between the two?

Answer: source /opt/ros/humble/setup.bash sets up the installed ROS 2 Humble environment and makes the standard ROS 2 packages and commands available. Meanwhile source install/local_setup.bash sets up the packages built in the current workspace so ROS 2 can find our custom packages, nodes, and launch files. The ROS installation is the underlay, while the workspace is an overlay.

### Q2: What does the ```queue_size``` argument control when creating a subscriber or a publisher? How does different ```queue_size``` affect how messages are handled?

Answer: The queue_size controls how many messages can wait in the publisher or subscriber queue. A larger queue can store more messages when messages arrive faster than they can be processed, but it uses more memory and may cause older messages to be processed later. A smaller queue uses less memory and keeps data more recent, but messages can be dropped if the queue becomes full.

### Q3: Do you have to call ```colcon build``` again after you've changed a launch file in your package? (Hint: consider two cases: calling ```ros2 launch``` in the directory where the launch file is, and calling it when the launch file is installed with the package.)

Answer: It depends on how the launch file is being used. If the launch file is run directly from the directory where it is located, colcon build is not required after making changes because the source file is being used directly. If the launch file is launched from the installed package using ros2 launch lab1_pkg lab1_launch.py, normally the package should be rebuilt so the updated launch file is installed. With --symlink-install, some changes may be reflected without rebuilding.
