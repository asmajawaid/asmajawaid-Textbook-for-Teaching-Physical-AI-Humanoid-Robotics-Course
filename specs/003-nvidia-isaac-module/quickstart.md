# Quickstart Guide: NVIDIA Isaac Module

This quickstart guide provides the essential steps to get you up and running with NVIDIA Isaac Sim and basic ROS 2 integration, allowing you to control a simulated robot.

## Prerequisites

-   **Operating System**: Ubuntu 22.04 LTS
-   **ROS 2 Distribution**: Humble Hawksbill
-   **NVIDIA Graphics Driver**: Latest stable version
-   **NVIDIA Omniverse Launcher**: Installed
-   **NVIDIA Isaac Sim**: Installed via Omniverse Launcher

## Step 1: Install ROS 2 Humble

Follow the official ROS 2 Humble installation guide for Ubuntu 22.04:
[https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html)

Ensure you install the `desktop` or `desktop-full` variant and source your setup files:
```bash
sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

sudo apt install software-properties-common -y
sudo add-apt-repository universe -y

sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

sudo apt update
sudo apt upgrade -y

sudo apt install ros-humble-desktop -y # Or ros-humble-desktop-full

echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

## Step 2: Install NVIDIA Isaac Sim

1.  Download and install the NVIDIA Omniverse Launcher from the [NVIDIA Developer website](https://developer.nvidia.com/nvidia-omniverse-platform).
2.  Launch Omniverse Launcher and install **Isaac Sim**. Ensure it's updated to the latest stable version.
3.  Once installed, launch Isaac Sim to ensure it runs correctly.

## Step 3: Install Isaac Sim ROS 2 Bridge Extension

The ROS 2 Bridge is typically included with Isaac Sim. Ensure it's enabled:

1.  Inside Isaac Sim, go to **Window > Extensions**.
2.  Search for "ROS 2" and ensure the "OmniGraph ROS 2 Bridge" extension is enabled.

## Step 4: Create a ROS 2 Workspace

Set up a standard ROS 2 workspace to build your robotics packages.

```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws
colcon build --symlink-install
echo "source ~/ros2_ws/install/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

## Step 5: Basic Robot Teleoperation Example

This example demonstrates controlling a simple differential drive robot in Isaac Sim using a ROS 2 teleoperation node.

### 5.1 Launch Isaac Sim with a Robot

1.  Launch Isaac Sim.
2.  Go to **File > Open**, and open an example scene with a mobile robot (e.g., `Isaac/Samples/ROS/Scenario/carter_nav.usd`).
3.  Ensure the ROS 2 Bridge is enabled (Step 3).

### 5.2 Create a ROS 2 Teleoperation Package

1.  Create a new ROS 2 Python package in your `~/ros2_ws/src` directory:
    ```bash
    cd ~/ros2_ws/src
    ros2 pkg create --build-type ament_python my_teleop
    ```
2.  Edit `~/ros2_ws/src/my_teleop/my_teleop/teleop_node.py` with the following content:
    ```python
    #!/usr/bin/env python3

    import rclpy
from rclpy.node import Node
    from geometry_msgs.msg import Twist
    import sys, select, tty, termios

    class TeleopPublisher(Node):
        def __init__(self):
            super().__init__('teleop_publisher')
            self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
            self.timer = self.create_timer(0.1, self.publish_twist)
            self.linear_speed = 0.5
            self.angular_speed = 0.5
            self.key = ''
            self.settings = termios.tcgetattr(sys.stdin)
            self.get_logger().info('Teleop node started. Use WASD to control, Q to quit.')

        def get_key(self):
            tty.setraw(sys.stdin.fileno())
            select.select([sys.stdin], [], [], 0)
            key = sys.stdin.read(1)
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.settings)
            return key

        def publish_twist(self):
            twist = Twist()
            self.key = self.get_key()

            if self.key == 'w':
                twist.linear.x = self.linear_speed
            elif self.key == 's':
                twist.linear.x = -self.linear_speed
            elif self.key == 'a':
                twist.angular.z = self.angular_speed
            elif self.key == 'd':
                twist.angular.z = -self.angular_speed
            elif self.key == 'q':
                self.get_logger().info('Exiting teleop node.')
                rclpy.shutdown()
                sys.exit(0) # Exit the script
            else:
                twist.linear.x = 0.0
                twist.angular.z = 0.0

            self.publisher_.publish(twist)

    def main(args=None):
        rclpy.init(args=args)
        node = TeleopPublisher()
        try:
            rclpy.spin(node)
        except SystemExit: # Catch the SystemExit from sys.exit(0)
            rclpy.logging.get_logger("teleop_publisher").info("Shutting down cleanly.")
        except KeyboardInterrupt:
            pass # Handle Ctrl+C gracefully
        finally:
            node.destroy_node()
            if rclpy.ok(): # Only shutdown if not already shutdown by sys.exit(0)
                rclpy.shutdown()


    if __name__ == '__main__':
        main()
    ```
3.  Edit `~/ros2_ws/src/my_teleop/setup.py` to add the executable:
    ```python
    from setuptools import setup
    import os
    from glob import glob

    package_name = 'my_teleop'

    setup(
        name=package_name,
        version='0.0.0',
        packages=[package_name],
        data_files=[
            ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
            ('share/' + package_name, ['package.xml']),
            (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')), # Add this line for launch files
        ],
        install_requires=['setuptools'],
        zip_safe=True,
        maintainer='your_name',
        maintainer_email='your_email@example.com',
        description='TODO: Package description',
        license='TODO: License declaration',
        tests_require=['pytest'],
        entry_points={
            'console_scripts': [
                'teleop_node = my_teleop.teleop_node:main',
            ],
        },
    )
    ```
4.  Build your workspace:
    ```bash
    cd ~/ros2_ws
    colcon build --packages-select my_teleop
    source install/setup.bash
    ```

### 5.3 Run Teleoperation

1.  In your terminal, navigate to your ROS 2 workspace and source the setup files:
    ```bash
    cd ~/ros2_ws
    source install/setup.bash
    ```
2.  Run the teleoperation node:
    ```bash
    ros2 run my_teleop teleop_node
    ```
3.  Switch focus to the terminal running the teleop node and use 'w', 'a', 's', 'd' keys to control the robot in Isaac Sim. Press 'q' to quit.

This concludes the quickstart. You should now be able to control a robot in NVIDIA Isaac Sim using ROS 2.