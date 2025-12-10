# Quickstart Guide: Module 4 - Vision-Language-Action (VLA)

This quickstart guide provides the essential steps to get you up and running with a basic Vision-Language-Action (VLA) pipeline, allowing you to issue voice commands to a simulated robot and see it react.

## Prerequisites

-   **Operating System**: Ubuntu 22.04 LTS
-   **ROS 2 Distribution**: Humble Hawksbill
-   **NVIDIA Graphics Driver**: Latest stable version
-   **NVIDIA Omniverse Launcher**: Installed
-   **NVIDIA Isaac Sim**: Installed via Omniverse Launcher
-   **Python 3.8+**: With `pip` installed.
-   **OpenAI API Key** (for Whisper and/or GPT models) **OR** local Whisper installation.
-   **LLM API Key** (e.g., OpenAI, Anthropic, Google) for task planning.

## Step 1: Core Environment Setup

Ensure your ROS 2 Humble and NVIDIA Isaac Sim environment is already set up as detailed in **Module 1 (ROS 2 Basics)** and **Module 3 (NVIDIA Isaac Module)** quickstart guides.

1.  **Install ROS 2 Humble**: Follow official instructions, ensure `ros-humble-desktop` is installed.
2.  **Install NVIDIA Isaac Sim**: Via Omniverse Launcher, ensure ROS 2 Bridge is enabled.
3.  **Create ROS 2 Workspace**: `~/ros2_ws` with `colcon build`.

## Step 2: Install OpenAI Whisper (Local)

For local speech-to-text, we'll use `whisper.cpp` via a Python binding. This avoids API costs and dependencies.

1.  **Clone `whisper.cpp`**:
    ```bash
    cd ~
    git clone https://github.com/ggerganov/whisper.cpp.git
    cd whisper.cpp
    # Build the C++ library
    make -j
    ```
2.  **Download a Model**:
    ```bash
    bash ./models/download-ggml-model.sh base.en
    # Or medium.en for better accuracy, but higher resource usage
    ```
3.  **Install Python Bindings**:
    ```bash
    pip install openai-whisper
    pip install git+https://github.com/openai/whisper.git
    ```
    *(Note: You may need to `pip install setuptools-rust` first)*

## Step 3: Configure LLM API Access

You'll need an API key for your chosen Large Language Model (e.g., OpenAI GPT, Anthropic Claude, Google Gemini).

1.  **Get API Key**: Obtain your API key from your chosen provider.
2.  **Set Environment Variable**: For security, store your API key as an environment variable.
    ```bash
    echo "export OPENAI_API_KEY='your_openai_api_key_here'" >> ~/.bashrc
    # Or for Gemini:
    echo "export GEMINI_API_KEY='your_gemini_api_key_here'" >> ~/.bashrc
    source ~/.bashrc
    ```
3.  **Install Python Client Library**:
    ```bash
    # For OpenAI
    pip install openai
    # For Google Gemini
    pip install google-generativeai
    # For Anthropic Claude
    pip install anthropic
    ```

## Step 4: Create ROS 2 VLA Pipeline Package

We'll create a ROS 2 package to orchestrate the VLA pipeline.

1.  **Create Package**:
    ```bash
    cd ~/ros2_ws/src
    ros2 pkg create --build-type ament_python vla_robot
    ```
2.  **Define Action Primitives**: Create a file `~/ros2_ws/src/vla_robot/vla_robot/action_primitives.py`
    ```python
    # Placeholder for action primitives
    # In a real system, these would call ROS 2 topics/services/actions
    class ActionPrimitives:
        def __init__(self):
            print("Initializing Action Primitives...")

        def move_joint(self, joint_name: str, position: float):
            print(f"Executing: Move joint '{joint_name}' to {position} radians")
            # TODO: Publish ROS 2 command to Isaac Sim
            return {"success": True, "message": f"Joint {joint_name} moved."}

        def say(self, text: str):
            print(f"Robot says: {text}")
            # TODO: Integrate with Text-to-Speech
            return {"success": True, "message": "Text spoken."}

        # Add more primitives as needed, e.g., navigate_to, grasp, pick_up
    ```
3.  **Create VLA Orchestrator Node**: Create a file `~/ros2_ws/src/vla_robot/vla_robot/vla_node.py`
    ```python
    #!/usr/bin/env python3

    import rclpy
    from rclpy.node import Node
    from std_msgs.msg import String
    import openai # or google.generativeai, anthropic
    import whisper
    import numpy as np
    import audioop
    import pyaudio
    import json # For parsing LLM response
    from vla_robot.action_primitives import ActionPrimitives

    class Vlanode(Node):
        def __init__(self):
            super().__init__('vla_node')
            self.get_logger().info("VLA Node Started.")

            # 1. Initialize Whisper (Local)
            self.get_logger().info("Loading local Whisper model...")
            self.whisper_model = whisper.load_model("base.en") # or "medium.en"
            self.get_logger().info("Whisper model loaded.")

            # 2. Initialize LLM Client (e.g., OpenAI GPT-4o)
            self.llm_client = openai.OpenAI() # Replace with your LLM client

            # 3. Initialize Audio Input (for microphone)
            self.p = pyaudio.PyAudio()
            self.stream = self.p.open(format=pyaudio.paInt16,
                                    channels=1,
                                    rate=16000,
                                    input=True,
                                    frames_per_buffer=1024)
            self.get_logger().info("Listening for commands... Press Ctrl+C to stop.")

            # 4. Action Primitives
            self.action_primitives = ActionPrimitives()

            # Timer to periodically check for voice commands
            self.create_timer(1.0, self.listen_and_process)

        def listen_and_process(self):
            # Read audio data from microphone
            data = self.stream.read(1024, exception_on_overflow=False)
            audio_np = np.frombuffer(data, dtype=np.int16).astype(np.float32) / 32768.0

            # Simple voice activity detection (VAD) - check if there's significant audio
            if np.abs(audio_np).mean() > 0.01: # Threshold for "speech"
                self.get_logger().info("Speech detected. Transcribing...")
                try:
                    # Convert numpy array to expected format if necessary
                    # For local whisper, you might need to save to a temp file or use specific bindings
                    # This example uses a simplified direct transcription for demonstration
                    # A more robust solution would buffer audio and pass the buffer
                    
                    # For demonstration, let's just simulate transcription
                    # text = self.whisper_model.transcribe(audio_np)["text"]
                    text = "simulate pick up red cube" # Placeholder for actual transcription
                    self.get_logger().info(f"Transcribed: {text}")

                    # If valid text, send to LLM
                    if text:
                        self.process_command_with_llm(text)

                except Exception as e:
                    self.get_logger().error(f"Whisper transcription failed: {e}")
            
        def process_command_with_llm(self, command_text: str):
            self.get_logger().info(f"Sending to LLM: {command_text}")
            
            # Example prompt for LLM
            prompt = f"""
            You are a robot assistant. Your available actions are:
            - move_joint(joint_name: str, position: float): Moves a robot joint to a specified position.
            - say(text: str): Makes the robot speak the given text.

            Current robot state: (Assume robot is in a neutral pose, can see objects)

            Based on the user command, generate a JSON object with a 'plan' key, which is a list of actions to execute.
            Example: {{"plan": [{{"action": "say", "params": {{"text": "Hello!"}}}}]}}
            User command: {command_text}
            """

            try:
                # Replace with actual LLM API call
                response = self.llm_client.chat.completions.create(
                    model="gpt-4o", # Replace with your model
                    messages=[
                        {"role": "system", "content": "You are a helpful robot assistant."},
                        {"role": "user", "content": prompt}
                    ],
                    response_format={"type": "json_object"}
                )
                llm_response_content = response.choices[0].message.content
                self.get_logger().info(f"LLM Response: {llm_response_content}")

                task_plan = json.loads(llm_response_content)
                self.execute_plan(task_plan)

            except Exception as e:
                self.get_logger().error(f"LLM processing failed: {e}")

        def execute_plan(self, task_plan: dict):
            if "plan" in task_plan:
                for action_item in task_plan["plan"]:
                    action_name = action_item.get("action")
                    params = action_item.get("params", {})
                    
                    if hasattr(self.action_primitives, action_name):
                        result = getattr(self.action_primitives, action_name)(**params)
                        self.get_logger().info(f"Executed {action_name} with params {params}: {result}")
                    else:
                        self.get_logger().warning(f"Unknown action primitive: {action_name}")
            else:
                self.get_logger().warning("No 'plan' found in LLM response.")


    def main(args=None):
        rclpy.init(args=args)
        node = Vlanode()
        rclpy.spin(node)
        node.destroy_node()
        rclpy.shutdown()

    if __name__ == '__main__':
        main()
    ```
4.  **Update `~/ros2_ws/src/vla_robot/setup.py`**:
    ```python
    from setuptools import setup
    import os
    from glob import glob

    package_name = 'vla_robot'

    setup(
        name=package_name,
        version='0.0.0',
        packages=[package_name],
        data_files=[
            ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
            ('share/' + package_name, ['package.xml']),
            (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        ],
        install_requires=['setuptools', 'rclpy', 'std_msgs', 'openai-whisper', 'openai', 'pyaudio', 'numpy'], # Add required packages
        zip_safe=True,
        maintainer='your_name',
        maintainer_email='your_email@example.com',
        description='VLA Robot ROS 2 Package',
        license='TODO: License declaration',
        tests_require=['pytest'],
        entry_points={
            'console_scripts': [
                'vla_node = vla_robot.vla_node:main',
            ],
        },
    )
    ```
5.  **Build your workspace**:
    ```bash
    cd ~/ros2_ws
    colcon build --packages-select vla_robot
    source install/setup.bash
    ```

## Step 5: Run the VLA Pipeline

1.  **Launch Isaac Sim**: Start Isaac Sim with your simulated humanoid robot. Ensure the ROS 2 Bridge is enabled and your robot is configured to receive commands (e.g., `/joint_states` or `/cmd_vel`).
2.  **Run VLA Node**: In a terminal, navigate to your ROS 2 workspace and source:
    ```bash
    cd ~/ros2_ws
    source install/setup.bash
    ros2 run vla_robot vla_node
    ```
3.  **Speak Commands**: With the VLA node running, speak commands into your microphone (e.g., "move shoulder joint to 0.5", "make the robot say hello world"). Observe the VLA node's output and the robot's reaction in Isaac Sim.

This concludes the quickstart. You should now have a basic VLA pipeline running, demonstrating speech-to-action capabilities.
