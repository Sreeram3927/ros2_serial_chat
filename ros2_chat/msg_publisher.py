import rclpy
from std_msgs.msg import String

def main(args = None) :
    rclpy.init(args = args)
    
    node = rclpy.create_node('publisher_node')
    publisher = node.create_publisher(String, 'serial_chat', 10)
    
    while rclpy.ok():
        input_msg = input('Enter a message to publish: ')
        msg = String()
        msg.data = input_msg
        publisher.publish(msg)