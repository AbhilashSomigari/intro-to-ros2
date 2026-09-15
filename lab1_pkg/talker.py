import rclpy
from rclpy.node import Node
from ackermann_msgs.msg import AckermannDriveStamped


class Talker(Node):

    def __init__(self):
        super().__init__('talker')

        # Declare ROS parameters
        self.declare_parameter('v', 0.0)
        self.declare_parameter('d', 0.0)

        # Publisher to the "drive" topic
        self.publisher_ = self.create_publisher(
            AckermannDriveStamped,
            'drive',
            10
        )

        # 0.0 means publish whenever the executor can run the callback
        # i.e. as fast as possible
        self.timer = self.create_timer(0.0, self.timer_callback)

    def timer_callback(self):

        # Read current parameter values
        v = float(self.get_parameter('v').value)
        d = float(self.get_parameter('d').value)

        # Create Ackermann message
        msg = AckermannDriveStamped()

        msg.header.stamp = self.get_clock().now().to_msg()

        msg.drive.speed = v
        msg.drive.steering_angle = d

        # Publish
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    talker = Talker()

    rclpy.spin(talker)

    talker.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
