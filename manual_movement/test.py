import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32MultiArray

class TestSubscriber(Node):

    def __init__(self):
        super().__init__('test_subscriber')
        self.subscription = self.create_subscription(Int32MultiArray, '/movement/Controller', self.listener_callback, 1)

    def listener_callback(self, msg):
        print(msg)


def main(args=None):
    rclpy.init(args=args)

    test_subscriber = TestSubscriber()

    rclpy.spin(test_subscriber)

    test_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
