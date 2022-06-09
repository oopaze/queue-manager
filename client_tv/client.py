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


def get_env(var, default):
    return environ.get(var, default)


class Client(socket):
    OFF = "off"
    ON = "on"

    SERVER_IP = get_env("SERVER_IP", gethostbyname(gethostname()))
    SERVER_PORT = 50000

    TRANSFORM_TV_TEMPLATE = """{
        "action": "transform_tv_connection"
    }"""

    def __init__(self, callback: callable, family=AF_INET, type=SOCK_STREAM):
        super().__init__(family, type)
        self.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self._running = self.OFF
        self.callback = callback
        self.settimeout(1)

    @property
    def running(self):
        return self._running == self.ON

    def stop(self):
        self._running = self.OFF

    def start(self):
        self._running = self.ON

    def connect(self) -> None:
        super().connect((self.SERVER_IP, self.SERVER_PORT))
        self.send(self.TRANSFORM_TV_TEMPLATE.encode("utf8"))

    def run(self):
        self.start()
        self.connect()

        while self.running:
            try:
                ticket = loads(self.recv(2048).decode("utf8"))
                ticket = ticket.get("message", None)
            except (TimeoutError, ConnectionResetError):
                ticket = None

            if ticket and ticket != "A lista está vazia":
                self.callback(ticket)
