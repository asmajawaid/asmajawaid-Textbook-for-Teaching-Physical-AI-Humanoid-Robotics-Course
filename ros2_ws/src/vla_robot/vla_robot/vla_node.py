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
import os # Import os module for environment variable checking
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
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            self.get_logger().error("OPENAI_API_KEY environment variable not set. Please set it to use OpenAI services.")
            raise RuntimeError("OPENAI_API_KEY not configured.")
        self.llm_client = openai.OpenAI(api_key=api_key) # Replace with your LLM client

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

        # Prompt templates for different tasks
        self.prompt_templates = {
            "default": """
            You are a robot assistant. Your available actions are:
            - move_joint(joint_name: str, position: float): Moves a robot joint to a specified position.
            - say(text: str): Makes the robot speak the given text.

            Current robot state: (Assume robot is in a neutral pose, can see objects)

            Based on the user command, generate a JSON object with a 'plan' key, which is a list of actions to execute.
            Example: {{"plan": [{{"action": "say", "params": {{"text": "Hello!"}}}}]}}
            User command: {command_text}
            """,
            "navigation": """
            You are a robot assistant. Your available actions are:
            - navigate_to(x: float, y: float, z: float, yaw: float): Navigates the robot to a specified 3D pose (x, y, z) with a given yaw orientation.
            - say(text: str): Makes the robot speak the given text.

            Current robot state: (Assume robot is at (0,0,0) with no specific orientation)
            Available navigation targets: "kitchen", "living room", "bedroom"

            Based on the user command, generate a JSON object with a 'plan' key, which is a list of actions to execute.
            Example: {{"plan": [{{"action": "navigate_to", "params": {{"x": 1.0, "y": 0.0, "z": 0.0, "yaw": 0.0}}}}]}}
            User command: {command_text}
            """
            "manipulation": """
            You are a robot assistant. Your available actions are:
            - pick_up(object_id: str): Commands the robot to pick up a specified object.
            - place_down(location: str): Commands the robot to place down an object at a specified location.
            - say(text: str): Makes the robot speak the given text.

            Current robot state: (Assume robot can see objects and gripper is empty/holding an object)
            Available objects: "red cube", "green cylinder", "blue sphere"
            Available locations: "table", "box", "shelf"

            Based on the user command, generate a JSON object with a 'plan' key, which is a list of actions to execute.
            Example: {{"plan": [{{"action": "pick_up", "params": {{"object_id": "red cube"}}}}]}}
            User command: {command_text}
            """,
            # Add other templates for manipulation, etc.
        }

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
                self.get_logger().error(f"Whisper transcription failed: {e}. Please ensure the model is loaded correctly and audio input is valid.")
        
    def process_command_with_llm(self, command_text: str):
        self.get_logger().info(f"Sending to LLM: {command_text}")
        
        # Choose a prompt template based on command content
        if "navigate" in command_text.lower() or "go to" in command_text.lower():
            template_name = "navigation"
        else:
            template_name = "default"
            
        current_prompt_template = self.prompt_templates.get(template_name, "").format(command_text=command_text)

        if not current_prompt_template:
            self.get_logger().error(f"No suitable prompt template found for {template_name}.")
            return

        # Example prompt for LLM
        prompt = current_prompt_template

        try:
            # Replace with actual LLM API call
            response = self.llm_client.chat.completions.create(
                model="gpt-4o", # Replace with your model
                messages=[
                    {"role": "system", "content": "You are a helpful robot assistant. If a command is ambiguous, include an 'ambiguous': true field in your JSON response along with a 'clarification_question' string. Otherwise, provide a 'plan' key."},
                    {"role": "user", "content": prompt}
                ],
                response_format={"type": "json_object"}
            )
            llm_response_content = response.choices[0].message.content
            self.get_logger().info(f"LLM Response: {llm_response_content}")

            task_plan = json.loads(llm_response_content)
            
            if task_plan.get("ambiguous", False):
                clarification_question = task_plan.get("clarification_question", "The command was ambiguous. Please rephrase.")
                self.get_logger().warning(f"Ambiguity detected: {clarification_question}")
                self.action_primitives.say(clarification_question)
            else:
                self.execute_plan(task_plan)

        except openai.APIConnectionError as e:
            self.get_logger().error(f"LLM API Connection Error: Could not connect to OpenAI API. {e}")
            self.action_primitives.say("I'm having trouble connecting to the internet. Please check my connection.")
        except openai.RateLimitError as e:
            self.get_logger().error(f"LLM API Rate Limit Exceeded: {e}")
            self.action_primitives.say("I'm receiving too many requests right now. Please try again in a moment.")
        except openai.APIError as e:
            self.get_logger().error(f"LLM API Error: {e}")
            self.action_primitives.say(f"I encountered an API error: {e.message}. Please try again.")
        except json.JSONDecodeError as e:
            self.get_logger().error(f"LLM Response JSON Decode Error: Invalid JSON received from LLM. {e}")
            self.action_primitives.say("I received an unreadable response from my brain. Please try your command again.")
        except Exception as e:
            self.get_logger().error(f"An unexpected error occurred during LLM processing: {e}")
            self.action_primitives.say("I encountered an unexpected error. Please try your command again.")

    def execute_plan(self, task_plan: dict):
        if "plan" in task_plan and isinstance(task_plan["plan"], list):
            for i, action_item in enumerate(task_plan["plan"]):
                if not isinstance(action_item, dict):
                    self.get_logger().warning(f"Invalid action item format at index {i}: Expected dictionary, got {type(action_item).__name__}. Skipping.")
                    continue
                
                action_name = action_item.get("action")
                params = action_item.get("params", {})
                
                if not isinstance(action_name, str):
                    self.get_logger().warning(f"Invalid 'action' in item at index {i}: Expected string, got {type(action_name).__name__}. Skipping.")
                    continue
                if not isinstance(params, dict):
                    self.get_logger().warning(f"Invalid 'params' in item at index {i}: Expected dictionary, got {type(params).__name__}. Skipping.")
                    continue

                try:
                    if hasattr(self.action_primitives, action_name):
                        result = getattr(self.action_primitives, action_name)(**params)
                        self.get_logger().info(f"Executed {action_name} with params {params}: {result}")
                        if not result.get("success", False):
                            error_message = result.get("message", "Unknown error during action execution.")
                            self.get_logger().error(f"Action '{action_name}' failed: {error_message}")
                            self.action_primitives.say(f"I encountered an error while trying to {action_name}. {error_message} Please give me a new command.")
                            # Stop further plan execution on failure for this simple example
                            break 
                    else:
                        self.get_logger().warning(f"Unknown action primitive: {action_name}")
                        self.action_primitives.say(f"I don't know how to perform the action: {action_name}.")
                        break # Stop further plan execution on unknown action
                except TypeError as e:
                    self.get_logger().error(f"Action '{action_name}' called with invalid parameters: {e}. Check LLM's generated parameters for '{action_name}'.")
                    self.action_primitives.say(f"I received invalid parameters for the action '{action_name}'. Please try your command again.")
                    break
                except Exception as e:
                    self.get_logger().error(f"An unexpected error occurred while executing action '{action_name}': {e}")
                    self.action_primitives.say(f"An unexpected error occurred during action '{action_name}'. Please try your command again.")
                    break
        else:
            self.get_logger().warning("No valid 'plan' found in LLM response or 'plan' is not a list.")
            self.action_primitives.say("I could not generate a valid plan for your command. Please try again.")


def main(args=None):
    rclpy.init(args=args)
    node = Vlanode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
