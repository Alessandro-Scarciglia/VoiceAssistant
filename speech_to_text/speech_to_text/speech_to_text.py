#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import speech_recognition as sr
from custom_if.srv import SendSentence
from functools import partial
import time


### Node class
class SpeechToText(Node):
	def __init__(self):
		super().__init__("stt_node")
		self.get_logger().info("STT node is up.")
		self.stt = sr.Recognizer()
		
		# Methods
		self.listen_to_user()


	## Listen and write
	def listen_to_user(self):

		self.call_nlu("Welcome")

		# Inner loop
		while True:
			with sr.Microphone() as source:
				self.stt.adjust_for_ambient_noise(source, duration=0.2)
				audio = self.stt.listen(source)

			try:
				sentence = "{0}".format(self.stt.recognize_google(audio, language="it-IT"))
				if 'Marvin' in sentence.split(" "):
					self.call_nlu(sentence)

			except sr.UnknownValueError:
				self.get_logger().warn("Waiting for a command.")
				
			except sr.RequestError as e:
				self.get_logger().error("STT Error; {0}".format(e))

	# Definition of the client request to the TTS
	def call_nlu(self, sentence):
		client = self.create_client(SendSentence, "send_command")
		while not client.wait_for_service(1.0):
			self.get_logger().warn("Waiting for Server...")

		request = SendSentence.Request()
		request.sentence = sentence
		future = client.call_async(request)
		future.add_done_callback(partial(self.callback_call_nlu, sentence=sentence))

	def callback_call_nlu(self, future, sentence):
		try:
			response = future.result()
			self.get_logger().info(f"Request solved: {response}")
	
		except Exception as e:
			self.get_logger().error("Request failed.")

def main(args=None):
	rclpy.init(args=args)
	node = SpeechToText()
	rclpy.spin(node)
	rclpy.shutdown()

if __name__ == "__main__":
	main()
