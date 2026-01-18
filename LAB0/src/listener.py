#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


def modify_message(s: str) -> str:
    # small modification: append a character + swap first two letters (if possible)
    if len(s) >= 2:
        s = s[1] + s[0] + s[2:]
    return s + "!"


class MyListener(Node):
    def __init__(self):
        super().__init__('my_listener')
        self.subscription = self.create_subscription(
            String,
            'chatter',
            self.callback,
            10
        )

    def callback(self, msg: String):
        modified = modify_message(msg.data)
        self.get_logger().info(f"I heard {modified}")


def main(args=None):
    rclpy.init(args=args)
    node = MyListener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
