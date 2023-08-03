#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class NodePublisher(Node):
    def __init__(self):
        super().__init__('node_publisher') # type: ignore
        self.count = 1
        self.publisher = self.create_publisher(
            String,
            "/messages",
            10
        )
        self.timer = self.create_timer(0.5, self.send_message)

    def send_message(self):
        message = String()
        message.data = str(self.count)+ ". " + input()
        self.count += 1
        self.publisher.publish(message)
        self.get_logger().info(f"Sending message: {message.data}")


def main(args=None):
    rclpy.init(args=args)

    publisher = NodePublisher()
    rclpy.spin(publisher)

    rclpy.shutdown()




if __name__ == "__main__":
    main()