import rclpy
from geometry_msgs.msg import Twist
from time import sleep

def run_robot():
    rclpy.init()

    node = rclpy.create_node('differential_robot')
    pub = node.create_publisher(Twist, '/cmd_vel', 10)

    while rclpy.ok():
        velocity_msg = Twist()
        velocity_msg.linear.x = 0.2
        velocity_msg.angular.z = 0.0
        pub.publish(velocity_msg)
        sleep(0.1)
    
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    run_robot()