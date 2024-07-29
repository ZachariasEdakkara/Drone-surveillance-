#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import os

class ImageSaver:
    def __init__(self):
        rospy.init_node('image_saver', anonymous=True)
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber('/camera/image_raw', Image, self.callback)
        self.image_count = 0
        self.save_path = '/tmp/images/'
        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)

    def callback(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
            filename = os.path.join(self.save_path, f'image_{self.image_count}.jpg')
            cv2.imwrite(filename, cv_image)
            self.image_count += 1
        except Exception as e:
            rospy.logerr("Error: %s", str(e))

    def run(self):
        rospy.spin()

if __name__ == '__main__':
    image_saver = ImageSaver()
    image_saver.run()

