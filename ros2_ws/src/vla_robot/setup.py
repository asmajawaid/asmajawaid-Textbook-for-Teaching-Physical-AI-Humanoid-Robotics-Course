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
