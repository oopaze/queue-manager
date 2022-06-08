from json import loads
from socket import socket, AF_INET, SOCK_STREAM
from typing import Callable


class Client(socket):
    SERVER_IP = "127.0.0.1"
    SERVER_PORT = 50000

    def __init__(self, family=AF_INET, type=SOCK_STREAM, *args, **kwargs):
        super().__init__(family, type, *args, **kwargs)

    def connect(self) -> None:
        return super().connect((self.SERVER_IP, self.SERVER_PORT))

    def send_message(self, message: str, callback: Callable):
        self.send(message)
        received_message = loads(self.recv(2048).decode("utf8"))
        callback(received_message)
