# VLA Interfaces for Module 4: Vision-Language-Action (VLA)

This document outlines the key communication interfaces and conceptual "contracts" that form the Vision-Language-Action (VLA) pipeline. These are categorized by the primary component they connect to or represent.

## 1. Speech-to-Text Interface (e.g., OpenAI Whisper)

This interface handles the conversion of spoken audio commands into textual representations.

-   **Input**: Raw audio stream (e.g., WAV, MP3, or directly from microphone).
    -   **Format**: Audio file or live stream.
    -   **Parameters**: Language (e.g., `en-US`), sampling rate, audio format.
-   **Output**: Text transcription.
    -   **Format**: String.
    -   **Parameters**: Confidence score, timestamps per word (optional).
-   **Integration Points**:
    -   **API (e.g., OpenAI Whisper API)**: HTTP POST request with audio data, JSON response with text.
    -   **Local Model (e.g., `whisper.cpp` via Python binding)**: Function call with audio data, string return.
    -   **ROS 2 Node**: Publishes `audio_common_msgs/msg/AudioData` or similar to a Whisper-processing node, which then publishes `std_msgs/msg/String` or custom `vla_msgs/msg/Transcription` messages.

## 2. Large Language Model (LLM) Interface (e.g., GPT-4o, Claude 3.5, Gemini 1.5)

This interface handles the high-level task planning and decomposition based on natural language text commands and environmental context.

-   **Input**: Structured text prompt.
    -   **Format**: String (often following a specific `Prompt Template`).
    -   **Parameters/Context**:
        -   User text command (e.g., "pick up the red cube").
        -   Available `Action Primitives` (names, descriptions, parameters).
        -   Current `Robot State` (e.g., object locations, robot pose).
        -   Safety constraints and system persona.
        -   Few-shot examples of desired input/output.
-   **Output**: Structured `Task Plan`.
    -   **Format**: JSON, Markdown list, or other parseable structure.
    -   **Content**: Sequence of `Action Primitives` with parameters.
-   **Integration Points**:
    -   **API (e.g., OpenAI API, Google Gemini API)**: HTTP POST request with prompt, JSON response with generated text.
    -   **Python Library**: SDK calls (e.g., `client.chat.completions.create()`).
    -   **ROS 2 Service/Action**: A ROS 2 node wrapping the API call, exposing a service (`vla_msgs/srv/PlanTask`) or action (`vla_msgs/action/ExecuteTask`) that takes the text command and returns the plan.

## 3. ROS 2 Action Primitive Interfaces

These are the low-level robot control interfaces that `Action Primitives` map to. They abstract away the robot-specific implementations.

-   **`navigateTo` Primitive**:
    -   **Purpose**: Move the robot to a specified 2D or 3D pose.
    -   **ROS 2 Interface**: `nav2_msgs/action/NavigateToPose` action.
    -   **Input**: `geometry_msgs/msg/PoseStamped` (target pose).
    -   **Output**: `Result` indicating success/failure.
-   **`grasp` Primitive**:
    -   **Purpose**: Command a robotic gripper to grasp an object.
    -   **ROS 2 Interface**: Often a custom ROS 2 service (e.g., `vla_msgs/srv/GraspObject`) or a simple topic (`std_msgs/msg/Bool` on `/gripper_command`). Could also be integrated with MoveIt 2.
    -   **Input**: `vla_msgs/msg/GraspTarget` (object ID, pose) or `std_msgs/msg/Bool` (open/close).
    -   **Output**: Success/failure.
-   **`place` Primitive**:
    -   **Purpose**: Command a robotic gripper to release an object at a specified location.
    -   **ROS 2 Interface**: Similar to `grasp`, a custom service or MoveIt 2 integration.
    -   **Input**: `vla_msgs/msg/PlaceTarget` (target pose).
    -   **Output**: Success/failure.
-   **`moveJoints` Primitive**:
    -   **Purpose**: Move specific robot joints to target positions.
    -   **ROS 2 Interface**: `control_msgs/action/FollowJointTrajectory` action or direct topic publication to joint controllers.
    -   **Input**: `trajectory_msgs/msg/JointTrajectory` or `sensor_msgs/msg/JointState`.
    -   **Output**: Success/failure.
-   **Perception Feedback**:
    -   **Purpose**: Obtain current information about the environment (e.g., object detection results).
    -   **ROS 2 Interface**: `sensor_msgs/msg/Image`, `sensor_msgs/msg/PointCloud2`, custom `vla_msgs/msg/ObjectDetection` topics or services.

## 4. Feedback / Clarification Interface

Allows the robot to provide verbal or textual feedback to the human user.

-   **Input**: Text message from robot (e.g., "Which block do you mean?").
-   **Output**: Spoken audio (via Text-to-Speech) or displayed text.
-   **Integration Points**:
    -   **Text-to-Speech (TTS) API/Local Model**: Function call with text, audio stream output.
    -   **ROS 2 Node**: Publishes `std_msgs/msg/String` to a TTS-processing node, which then plays the audio.
    -   **Console Output**: Simple `print()` statements.
