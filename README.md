# Textbook for Teaching Physical AI & Humanoid Robotics

Welcome to the official repository for the "Textbook for Teaching Physical AI & Humanoid Robotics." This project provides a comprehensive, hands-on curriculum for learning the principles of Physical AI by building a complete software stack for a robotic arm.

This textbook is built as a Docusaurus website, providing an interactive and engaging learning experience.

## Project Overview

This course is designed to bridge the gap between the latest advancements in AI and the practical challenges of robotics. We explore the convergence of:

-   **Humanoid Robotics:** Understanding the mechanics and control of robotic systems.
-   **AI Perception:** Enabling robots to "see" and interpret their environment.
-   **Large Language Models (LLMs):** Leveraging the power of models like GPT-4 to provide reasoning and natural language understanding capabilities to our robotic systems.

The core of this course is the development of a **Visual-Language-Action (VLA)** model, which allows a user to instruct a robotic arm using natural language.

## Prerequisites

To successfully follow this course and run the provided code, you will need a development environment with **ROS 2 (Humble)** installed.

### Environment Setup (WSL 2 Recommended)

For Windows users, it is highly recommended to use **Windows Subsystem for Linux (WSL 2)** with an **Ubuntu 22.04** distribution. This provides the most stable and well-supported environment for ROS 2 development.

1.  **Install WSL 2:** Follow the official Microsoft documentation to [install WSL 2](https://learn.microsoft.com/en-us/windows/wsl/install).
2.  **Install Ubuntu 22.04:** Once WSL is installed, install the "Ubuntu 22.04 LTS" distribution from the Microsoft Store.
3.  **Install ROS 2 Humble:** Inside your Ubuntu 22.04 environment, follow the official ROS 2 documentation to [install ROS 2 Humble Hawksbill](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html).

### ROS 2 Workspace

The ROS 2 packages for this project are located in the `ros2_ws` directory. To build and use them, you will need to source your ROS 2 setup file and build the workspace:

```bash
# Navigate to your ROS 2 workspace
cd ros2_ws

# Source the ROS 2 environment
source /opt/ros/humble/setup.bash

# Build the workspace
colcon build

# Source the local workspace
source install/setup.bash
```

## Running the Docusaurus Website

The textbook is a Docusaurus website located in the `website` directory.

### Prerequisites

-   **Node.js:** You need Node.js version 20.0 or higher.

### Installation

1.  Navigate to the `website` directory:
    ```bash
    cd website
    ```
2.  Install the dependencies:
    ```bash
    npm install
    ```

### Running the Development Server

To start the local development server and view the textbook in your browser:

```bash
npm run start
```

This will open a browser window at `http://localhost:3000`. The website will automatically reload as you make changes to the source files.

### Building the Website

To create a static build of the website for deployment:

```bash
npm run build
```

The build artifacts will be located in the `website/build` directory.
