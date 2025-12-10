import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */
const sidebars: SidebarsConfig = {
  tutorialSidebar: [
    'introduction',
    'hardware-requirements',
    {
      type: 'category',
      label: 'Chapter 1: Module 1 - The Robotic Nervous System (ROS 2)',
      link: {
        type: 'doc',
        id: 'ros-2-basics-intro',
      },
      items: [
        'module-1-ros2/ros2-architecture',
        'module-1-ros2/nodes-topics-services-actions',
        'module-1-ros2/packages-and-build-system',
        'module-1-ros2/launch-files',
        'module-1-ros2/urdf-robot-description',
      ],
    },
    {
      type: 'category',
      label: 'Chapter 2: Module 2 - The Digital Twin (Simulation)',
      link: {
        type: 'doc',
        id: 'module-2-digital-twin/gazebo-physics-simulation',
      },
      items: [
        'module-2-digital-twin/sensor-simulation-lidar-realsense',
        'module-2-digital-twin/unity-visualization',
      ],
    },
    {
      type: 'category',
      label: 'Chapter 3: Module 3 - The AI-Robot Brain (NVIDIA Isaac™)',
      link: {
        type: 'doc',
        id: 'module-3-nvidia-isaac/isaac-sim-synthetic-data',
      },
      items: [
        'module-3-nvidia-isaac/isaac-ros-vslam-nav2',
        'module-3-nvidia-isaac/reinforcement-learning',
        'module-3-nvidia-isaac/sim-to-real',
      ],
    },
    {
      type: 'category',
      label: 'Chapter 4: Module 4 - Vision-Language-Action (VLA)',
      link: {
        type: 'doc',
        id: 'vla_module',
      },
      items: [
        'module-4-vla/whisper-integration',
        'module-4-vla/conversational-planning-llm-integration',
        'module-4-vla/capstone-project-overview',
      ],
    },
    {
      type: 'category',
      label: 'Chapter 5: Humanoid Robot Development',
      link: {
        type: 'doc',
        id: 'humanoid-kinematics-intro',
      },
      items: [
        'module-5-humanoid-dev/kinematics-and-dynamics',
        'module-5-humanoid-dev/bipedal-locomotion',
        'module-5-humanoid-dev/manipulation-and-grasping',
        'module-5-humanoid-dev/hri-design',
      ],
    },
    {
      type: 'category',
      label: 'Chapter 6: Conversational Robotics',
      link: {
        type: 'doc',
        id: 'module-6-conversational-robotics/gpt-integration',
      },
      items: [
        'module-6-conversational-robotics/speech-and-nlp',
        'module-6-conversational-robotics/multimodal-interaction',
      ],
    },
    {
        type: 'category',
        label: 'Appendix: Tools and Setup',
        link: {
            type: 'doc',
            id: 'appendix-intro',
        },
        items: [],
    },
  ],
};

export default sidebars;
