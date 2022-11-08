#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import speech_recognition as sr
from custom_if.srv import SendSentence
from functools import partial


### Node class
class NLUnderstanding(Node):
	def __init__(self):
		super().__init__("nlu_node")
		self.get_logger().info("NLU node is up.")

		# Service
		self.server = self.create_service(SendSentence, 'send_command', self.callback_command)

	# Server callbacks
	def callback_command(self, request, response):
		
		# So far the node simply writes down what has been said.
		# TODO: Implement here a link to all possible actions.
		self.get_logger().info(f"{request.sentence}")
		response.done = True
		return response
	

def main(args=None):
	rclpy.init(args=args)
	node = NLUnderstanding()
	rclpy.spin(node)
	rclpy.shutdown()

if __name__ == "__main__":
	main()
