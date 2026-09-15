import rclpy
from rclpy.node import Node
from ackermann_msgs.msg import AckermannDriveStamped


class Relay(Node):

    def __init__(self):
        super().__init__('relay')

        # Subscribe to drive
        self.subscription = self.create_subscription(
            AckermannDriveStamped,
            'drive',
            self.listener_callback,
            10
        )

        # Publish to drive_relay
        self.publisher_ = self.create_publisher(
            AckermannDriveStamped,
            'drive_relay',
            10
        )

    def listener_callback(self, msg):

        relay_msg = AckermannDriveStamped()

        relay_msg.header.stamp = self.get_clock().now().to_msg()

        # Multiply incoming values by 3
        relay_msg.drive.speed = msg.drive.speed * 3.0
        relay_msg.drive.steering_angle = (
            msg.drive.steering_angle * 3.0
        )

        self.publisher_.publish(relay_msg)


def main(args=None):
    rclpy.init(args=args)

    relay = Relay()

    rclpy.spin(relay)

    relay.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
