# ROS 2 Interfaces for Module 3: NVIDIA Isaac Module

This document outlines the key ROS 2 topics, services, and actions that will be utilized and demonstrated throughout the "NVIDIA Isaac Module" chapter. These interfaces facilitate communication between ROS 2 nodes and the NVIDIA Isaac Sim environment via the ROS 2 Bridge.

## 1. Topics

### 1.1 Command Topics (from ROS 2 to Isaac Sim)

-   **`/cmd_vel` (geometry_msgs/msg/Twist)**:
    -   **Description**: Publishes linear and angular velocity commands to control mobile robots (e.g., for teleoperation or navigation).
    -   **Usage in Chapter**: Used in User Story 1 (Basic Robot Control) for teleoperating a wheeled robot, and in User Story 3 (Autonomous Navigation) by Nav2.

-   **`/joint_states` (sensor_msgs/msg/JointState)**:
    -   **Description**: Publishes the state of robot joints (position, velocity, effort). While often published by the robot, it can also be commanded for direct joint control.
    -   **Usage in Chapter**: Relevant for User Story 5 (Manipulating Objects) for controlling robotic arm joints.

### 1.2 Sensor Data Topics (from Isaac Sim to ROS 2)

-   **`/scan` (sensor_msgs/msg/LaserScan)**:
    -   **Description**: Publishes 2D laser scan data, typically from a LiDAR sensor.
    -   **Usage in Chapter**: Used in User Story 2 (Integrate and Visualize Sensor Data) for visualizing LiDAR data in RViz and potentially by Nav2 for obstacle avoidance.

-   **`/camera/image_raw` (sensor_msgs/msg/Image)**:
    -   **Description**: Publishes raw image data from a camera sensor. (Note: topic name may vary based on camera configuration, e.g., `/front_camera/image_raw`).
    -   **Usage in Chapter**: Used in User Story 2 (Integrate and Visualize Sensor Data) for visualizing camera feeds in RViz and for synthetic data generation (User Story 4).

-   **`/camera/depth/image_raw` (sensor_msgs/msg/Image)**:
    -   **Description**: Publishes raw depth image data from a depth camera sensor.
    -   **Usage in Chapter**: Potentially used in User Story 2 for visualizing depth, and for synthetic data.

-   **`/tf` and `/tf_static` (tf2_msgs/msg/TFMessage)**:
    -   **Description**: Publishes coordinate frame transformations between different parts of the robot and the world. Essential for understanding robot pose and sensor data localization.
    -   **Usage in Chapter**: Implicitly used in all examples involving robot movement, sensor data, and navigation for correct frame transformations.

## 2. Services

-   **`/isaac_sim/simulation_clock` (rosgraph_msgs/msg/Clock)**:
    -   **Description**: Publishes the simulation time, crucial for time synchronization in ROS 2.
    -   **Usage in Chapter**: Mentioned as part of the simulation setup for accurate ROS 2 timestamping.

## 3. Actions

-   **`/navigate_to_pose` (nav2_msgs/action/NavigateToPose)**:
    -   **Description**: An action to command a robot to autonomously navigate to a specified pose in the map.
    -   **Usage in Chapter**: Central to User Story 3 (Autonomous Navigation) for integrating with the Nav2 stack.

-   **`/follow_joint_trajectory` (control_msgs/action/FollowJointTrajectory)**:
    -   **Description**: An action to command a robot's joints to follow a specified trajectory.
    -   **Usage in Chapter**: Potentially used in User Story 5 (Manipulating Objects) for controlling robotic arm movements in conjunction with MoveIt 2.
