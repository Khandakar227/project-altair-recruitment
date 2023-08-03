#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class NodeSubscriber(Node):
    def __init__(self):
        super().__init__('node_subscriber') # type: ignore
        self.subscription = self.create_subscription(
            String,
            "/messages",
            self.subscribe_cb,
            10
        )

    def subscribe_cb(self, msg:String):
        self.get_logger().info(f"Recieved: {msg.data}")

def main(args=None):
    print("Node Subscription Started")
    rclpy.init(args=args)
    subscriber = NodeSubscriber()
    rclpy.spin(subscriber)


    rclpy.shutdown()

if __name__ == "__main__":
    main()
