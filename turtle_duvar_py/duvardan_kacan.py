#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose


class DuvardanKacanKaplumbaga(Node):
    def __init__(self):
        super().__init__('duvardan_kacan_node')

        # Bonus: Hız ve sınır değerlerini parametre yapma
        self.declare_parameter('forward_speed', 2.0)
        self.declare_parameter('turn_speed', 1.5)
        self.declare_parameter('min_limit', 1.0)
        self.declare_parameter('max_limit', 10.0)

        # Abone (Subscriber): /turtle1/pose
        self.pose_subscriber = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.pose_callback,
            10
        )

        # Yayıncı (Publisher): /turtle1/cmd_vel
        self.cmd_vel_publisher = self.create_publisher(
            Twist,
            '/turtle1/cmd_vel',
            10
        )

        # Saniyede bir kez loglama
        self.log_timer = self.create_timer(1.0, self.log_konum)

        # Anlık konum alma
        self.current_x = 5.54
        self.current_y = 5.54
        self.pose_received = False

    def pose_callback(self, msg: Pose):
        self.current_x = msg.x
        self.current_y = msg.y
        self.pose_received = True

        forward_speed = self.get_parameter('forward_speed').value
        turn_speed = self.get_parameter('turn_speed').value
        min_limit = self.get_parameter('min_limit').value
        max_limit = self.get_parameter('max_limit').value

        cmd = Twist()

        # Duvar kontrol mantığı
        if (self.current_x < min_limit or self.current_x > max_limit or 
            self.current_y < min_limit or self.current_y > max_limit):
            cmd.linear.x = 0.5
            cmd.angular.z = turn_speed
        else:
            cmd.linear.x = forward_speed
            cmd.angular.z = 0.0

        self.cmd_vel_publisher.publish(cmd)

    def log_konum(self):
        if self.pose_received:
            self.get_logger().info(f'Kaplumbağa Konumu -> X: {self.current_x:.2f}, Y: {self.current_y:.2f}')


def main(args=None):
    rclpy.init(args=args)
    node = DuvardanKacanKaplumbaga()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
