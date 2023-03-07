import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial

class SerialNode(Node):
    
    def __init__(self):
        super().__init__('serial_node')

        self.serial_port = serial.Serial('/dev/ttyACM0', 9600)

        self.publisher_ = self.create_publisher(String, 'serial_data', 10)