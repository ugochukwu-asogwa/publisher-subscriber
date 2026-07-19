"""A simple subscriber node."""
import rclpy
from example_interfaces.msg import String
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node


class subscriber(Node):
    """Subscriber node to pull messages from topics."""

    def __init__(self):
        """Constructor"""
        super().__init__("subscriber")
        self._subscriber = self.create_subscription(String, "rob_test", self._listener_callback, 10)

    def _listener_callback(self, msg):
        """Prints message from topic in the console."""
        self.get_logger().info(f"Received information: {msg.data}")


def main(args=None):
    """Entry point"""
    try:
        rclpy.init()
        node = subscriber()
        rclpy.spin(node)

    except (KeyboardInterrupt, ExternalShutdownException):
        pass

    finally:
        if node is not None:
            node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()

