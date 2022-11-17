#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import speech_recognition as sr
from custom_if.srv import SendSentence
from functools import partial
from nl_understanding.tcp_client import GenericClient


### Node class
class NLUnderstanding(Node):
	def __init__(self):
		super().__init__("nlu_node")
		self.get_logger().info("NLU node is up.")
		self.client = GenericClient(host='localhost', port=50000)

		# Service
		self.server = self.create_service(SendSentence, 'send_command', self.callback_command)

	# Server callbacks
	def callback_command(self, request, response):
		self.client.send_request(1)
		self.get_logger().info("Request sent.")
		
		response.done = True
		return response
	

def main(args=None):
	rclpy.init(args=args)
	node = NLUnderstanding()
	rclpy.spin(node)
	rclpy.shutdown()

if __name__ == "__main__":
	main()
