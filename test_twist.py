import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class MyNode(Node):

    def __init__(self):
        super().__init__("my_node")
        self.publisher_ = self.create_publisher(Twist, "/cmd_vel", 10)
        self.timer_ = self.create_timer(0.1, self.timer_callback)
        self.current_time_ = self.get_clock().now()
        self.linear_velocity_ = 1.0
        self.elapsed_time_ = 0.0
        print("init node")

    def timer_callback(self):
        time_difference = self.get_clock().now() - self.current_time_
        self.elapsed_time_ = time_difference.nanoseconds / 1000000000.0

        if self.elapsed_time_ < 3.0:
            twist = Twist()
            twist.linear.x = self.linear_velocity_
            twist.angular.z = 0.0
            self.publisher_.publish(twist)
        else:
            twist = Twist()
            twist.linear.x = 0.0
            twist.angular.z = 0.0
            self.publisher_.publish(twist)
            self.timer_.cancel()

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()