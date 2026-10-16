import random

import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node

from example_interfaces.srv import AddTwoInts


class Client(Node):
    """A client to make a server call."""

    def __init__(self):
        super().__init__("client")
        self._client = self.create_client(AddTwoInts, "add_integer")

        while not self._client.wait_for_service(timeout_sec=2.0):
            self.get_logger().info("Waiting for service ...")
        
        self._timer = self.create_timer(2.0, self._timer_callback)
    
    def _timer_callback(self):
        req = AddTwoInts.Request()
        req.a = random.randint(0, 20)
        req.b = random.randint(0, 20)

        self.future = self._client.call_async(req)
        self.future.add_done_callback(self._response_callback)

    def _response_callback(self, future):
        """Log results when received in server"""
        try:
            resp = future.result()
            self.get_logger().info(f"Result: {resp.sum}")

        except Exception as e:
            self.get_logger().error(f"{str(e)}")



def main(args=None):
    """Entry point"""
    try:
        rclpy.init()
        node = Client()
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