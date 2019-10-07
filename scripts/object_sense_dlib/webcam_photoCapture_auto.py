#!/usr/bin/env python
import roslib
import cv2
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class AutoPhotoCapture(object):

	def __init__(self, 
				 video_source=0):

		self.video_capture = cv2.VideoCapture(video_capture)
		self.image_index = 0
		self.pub_img = rospy.Publisher('frame_chatter', Image, queue_size=10)
		self.pub_L_command = rospy.Publisher('keyboard_L_command', Int8, queue_size=10)
    	self.pub_R_command = rospy.Publisher('keyboard_R_command', Int8, queue_size=10)
		self.bridge = CvBridge()
		rospy.init_node('webcam_photoCapture_auto', anonymous=True)
		self.rate = rospy.Rate(25)

	def next_pos(self):
		for _ in range(10):
	        self.pub_L_command.publish(int(126))
	        self.pub_R_command.publish(int(126))
	        self.rate.sleep()	

	def back_pos(self):
		for _ in range(10):
	        self.pub_L_command.publish(int(-126))
	        self.pub_R_command.publish(int(-126))
	        self.rate.sleep()

	def get_image(self):
		self.image_index += 1
		ret, frame = video_capture.read()
		return frame

	def send_image(self, frame):
		self.pub_img.publish(self.bridge.cv2_to_imgmsg(frame))

	def main_loop(self):
		#frame = self.get_image()
		#self.send_image(frame)
		self.next_pos()	

# ======================================================================================================================
def webcam_photoCapture_auto():
    webcam_photoCapture_auto = AutoPhotoCapture().main_loop()

if __name__ == '__main__':
    try:
        webcam_photoCapture_auto()
    except rospy.ROSInterruptException:
        pass