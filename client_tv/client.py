from json import loads
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


class Client(socket):
    OFF = "off"
    ON = "on"
    SERVER_IP = gethostbyname(gethostname())
    SERVER_PORT = 50000

    TRANSFORM_TV_TEMPLATE = """{
        "action": "transform_tv_connection"
    }"""

    def __init__(self, callback: callable, family=AF_INET, type=SOCK_STREAM):
        super().__init__(family, type)
        self.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self._running = self.OFF
        self.callback = callback

    @property
    def running(self):
        return self._running == self.ON

    def connect(self) -> None:
        return super().connect((self.SERVER_IP, self.SERVER_PORT))

    def run(self):
        self._running = self.ON
        self.connect()
        self.send(self.TRANSFORM_TV_TEMPLATE.encode("utf8"))

        while self.running:
            try:
                ticket = loads(self.recv(2048).decode("utf8"))
                ticket = ticket.get("message", None)
            except:
                ticket = None

            if ticket:
                self.callback(ticket)
