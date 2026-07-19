"""A simple publisher node."""
import rclpy
from example_interfaces.msg import String
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node


class Publisher(Node):
    """Publisher node to periodically send string of text to the topic."""

    def __init__(self):
        """Constructor"""
        super().__init__("publisher")
        self._publisher = self.create_publisher(String, "rob_test", 10)
        self._timer = self.create_timer(5, self._timer_callback)
        self._counter = 0
        self.logger = self.get_logger()

    def _timer_callback(self):
        """Publishes a simple message to the specified topic."""
        msg = String()
        msg.data = f"Welcome to the new dispensation --> {self._counter}"
        self._publisher.publish(msg)
        self.logger.info(f"Publishing message: {msg.data}")
        self._counter += 1


def main():
    """Entry point for the publisher node."""
    try:
        rclpy.init()
        node = Publisher()
        rclpy.spin(node)  # Runs the node indefinitely in rclpy process.

    except (KeyboardInterrupt, ExternalShutdownException):
        pass

    finally:
        if node is not None:    
            node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == "__main__":
    main()
