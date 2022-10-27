#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import pyttsx3 as tts
from custom_if.srv import SendSentence
from functools import partial
 


class TextToSpeech(Node):
	def __init__(self):
		super().__init__("tts_node")
		self.get_logger().info("TTS node is up.")
		self.speaker = tts.init("espeak")
		self.speaker.setProperty('rate', 130)
		self.speaker.setProperty('voice', 'italian')

		# Service
		self.server = self.create_service(SendSentence, 'say_sentence', self.callback_saysentence)

	def callback_saysentence(self, request, response):
		self.speaker.say(request.sentence)
		self.speaker.runAndWait()
		response.done = True
		return response

def main(args=None):
	rclpy.init(args=args)
	node = TextToSpeech()
	rclpy.spin(node)
	rclpy.shutdown()

if __name__ == "__main__":
	main()
