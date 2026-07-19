# publisher-subscriber

A simple ROS 2 Python project demonstrating the fundamental communication model of ROS 2 using `rclpy`.

This project implements a publisher node and a subscriber node that communicate through a ROS 2 topic.

## Overview

ROS 2 applications are built around independent processes called **nodes** that communicate using topics, services, and actions.

In this project:

- The **Publisher node** generates and publishes messages.
- The **Subscriber node** listens to the topic and processes received messages.
- Communication is handled through ROS 2 middleware using the publish/subscribe architecture.

## Project Structure

```text
publisher-subscriber/
├── pub_sub_pkg/
│     ├── pub_sub_pkg/
│     │   ├── publisher.py
│     │   └── subscriber.py
│     ├── package.xml
│     └── setup.py
├── build/
├── install/
└── log/
```

## Technologies

- ROS 2
- Python
- rclpy
- colcon build system

## How It Works

### Publisher Node

The publisher creates a ROS 2 node and publishes messages to a topic.

```text
Publisher Node
       |
       | publishes messages
       ↓
    /topic_name
```

### Subscriber Node

The subscriber creates a ROS 2 node that listens to the same topic and receives messages.

```text
/topic_name
       |
       | receives messages
       ↓
Subscriber Node
```

## Build

Navigate to the ROS 2 workspace:

Build the package:

```bash
colcon build
```

Source the workspace:

```bash
source install/setup.bash
```

## Run

Open two separate terminals.

### Terminal 1 - Start Subscriber

```bash
ros2 run <package_name> subscriber
```

### Terminal 2 - Start Publisher

```bash
ros2 run <package_name> publisher
```

The subscriber will display messages published by the publisher node.

## Concepts Learned

- ROS 2 workspace structure
- Creating ROS 2 Python packages
- Building packages using `colcon`
- Creating nodes with `rclpy`
- Publishing messages through topics
- Subscribing to topics
- ROS 2 publish/subscribe communication architecture
