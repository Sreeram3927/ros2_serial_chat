import rclpy
from std_msg import Strings

def callback(msg) :
    print(msg)

def main(args = None):
    rclpy.init(args = args)
    
    node = rclpy.create_node('subscriber_node')
    subscription = node.create_subscription(String, 'serial_chat', callback, 10)
    
    while rclpy.ok():
        rclpy.spin_once(node)
        
    node.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__' :
    main()