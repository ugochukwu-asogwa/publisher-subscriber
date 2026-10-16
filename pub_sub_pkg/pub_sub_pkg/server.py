import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node

from example_interfaces.srv import AddTwoInts


class Server(Node):
    """Server to add two integers and respond with result."""

    def __init__(self):
        super().__init__("server")
        self.srv = self.create_service(
            AddTwoInts,
            'add_integer',
            self._server_callback,
        )

    def _server_callback(self, req, resp):
        """Responds with answer to request."""
        resp.sum = req.a + req.b
        self.get_logger().info(f"Received request: a = {req.a}, b = {req.b}")

        return resp


def main(args=None):
    """Entry point"""
    try:
        rclpy.init()
        node = Server()
        rclpy.spin(node)

    except (KeyboardInterrupt, ExternalShutdownException):
        pass

    finally:
        if node is not None:
            node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == "__main__":
    main()
