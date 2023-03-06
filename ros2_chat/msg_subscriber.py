import rclpy
from std.msg import Strings

def callback(msg) :
    print(msg)

def main(args = None):
    rclpy.init(args = args)
    
    node = rclpy.create_node('subscriber_node')
    subscription = node.create_subscription(String, 'serial_chat', callback, 10)