from json import loads
from os import environ
from socket import (
    gethostbyname,
    gethostname,
    socket,
    AF_INET,
    SOCK_STREAM,
    SOL_SOCKET,
    SO_REUSEADDR,
)
from typing import Callable


def get_env(var, default):
    return environ.get(var, default)


class Client(socket):
    SERVER_IP = get_env("SERVER_IP", gethostbyname(gethostname()))
    SERVER_PORT = 50000

    def __init__(self, family=AF_INET, type=SOCK_STREAM, *args, **kwargs):
        super().__init__(family, type, *args, **kwargs)
        self.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    def connect(self) -> None:
        return super().connect((self.SERVER_IP, self.SERVER_PORT))

    def send_message(self, message: str, callback: Callable):
        self.send(message)
        received_message = loads(self.recv(2048).decode("utf8"))
        callback(received_message)
