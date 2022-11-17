#!/usr/bin/env python3

import socket

# Parameters
MSG_SIZE = 1024


class GenericClient:
    """
        Generic client class accept as attributes:
            host: str the name of the local host ('localhost' by default)
            port: int the port number
        Returns:
            server response: bytes output of the method send_request
        """
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.msg_size = MSG_SIZE

    def send_request(self, request):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            
            # Send request
            sock.connect((self.host, self.port))
            sock.sendall(bytes(str(request), "utf-8"))

            # Get response and return
            res = sock.recv(self.msg_size)

            return res
