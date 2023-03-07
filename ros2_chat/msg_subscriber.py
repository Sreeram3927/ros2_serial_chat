import rclpy
from std_msgs.msg import String
from rclpy.node import Node
import serial


class SerialSub(Node):
    def __init__(self):
        super().__init__('node')

def callback(msg) :
    print(msg.data)

def main(args = None):
    rclpy.init(args = args)
    
    #node = rclpy.create_node('subscriber_node')
    subscription = node.create_subscription(String, 'serial_chat', callback, 10)
    
    while rclpy.ok():
        rclpy.spin_once(node)
        
    node.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__' :
    main()