import serial 

import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from geometry_msgs.msg import Twist

ser = serial.Serial('/dev/ttyUSB0', baudrate = 9600, timeout = 1)

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        # self.subscription = self.create_subscription(
        #     String,
        #     'topic',
        #     self.listener_callback,
        #     10)

        self.subscription = self.create_subscription(
            Twist,
            'cmd_vel',
            self.cmd_cb,6)            
        self.subscription  # prevent unused variable warning

    # def listener_callback(self, msg):
    #     self.get_logger().info('I heard: "%s"' % msg.data)

    def cmd_cb(self, msg):
        x = msg.linear.x
        az = msg.angular.z
        self.get_logger().info('I linear x: "%f"' % x)
        self.get_logger().info('I angular z: "%f"' % az)
        if x == 0:
            ser.write(b's')
        elif x > 0:
            ser.write(b'f')
        elif x < 0:
            ser.write(b'b')
        if az > 0:
            ser.write(b'r')
        elif az < 0:
            ser.write(b'l')                        

def main(args=None):
    rclpy.init(args=args)
    
    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
