import rclpy
from std.msg import Strings

def main(args = None):
    rclpy.init(args = args)
    
    node = rclpy.create_node('subscriber_node')
    subscription = node.create_subscription(String, 'serial_chat', , 10)