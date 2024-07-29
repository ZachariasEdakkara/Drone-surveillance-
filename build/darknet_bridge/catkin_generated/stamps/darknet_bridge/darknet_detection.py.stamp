#!/usr/bin/env python

import rospy
import subprocess
import os

class DarknetDetection:
    def __init__(self):
        rospy.init_node('darknet_detection', anonymous=True)
        self.image_path = '/tmp/images/'
        self.darknet_path = '/path/to/darknet'
        self.config_file = 'cfg/yolov3.cfg'
        self.weights_file = 'yolov3.weights'
        self.data_file = 'cfg/coco.data'

    def detect_objects(self):
        image_files = sorted([f for f in os.listdir(self.image_path) if f.endswith('.jpg')])
        for image_file in image_files:
            image_path = os.path.join(self.image_path, image_file)
            command = f'cd {self.darknet_path} && ./darknet detector test {self.data_file} {self.config_file} {self.weights_file} {image_path}'
            subprocess.run(command, shell=True)

    def run(self):
        rospy.loginfo("Starting object detection...")
        self.detect_objects()

if __name__ == '__main__':
    detector = DarknetDetection()
    detector.run()

