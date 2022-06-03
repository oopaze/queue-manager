from abc import abstractclassmethod
from socket import (
    AF_INET,
    SOL_SOCKET,
    SO_REUSEADDR,
    SOCK_DGRAM,
    socket,
    gethostname,
    gethostbyname,
)


class Socket(socket):
    ON = "on"
    OFF = "off"

    host = gethostbyname(gethostname())
    port = 5000
    _running = OFF

    def __init__(self, listen_amount: int = 3, bind: bool = True, *args, **kwargs):
        kwargs.update({"family": AF_INET, "type": SOCK_DGRAM})
        super().__init__(*args, **kwargs)

        if bind:
            self.bind()

    @property
    def running(self):
        return self._running == self.ON

    def bind(self):
        self.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        super().bind((self.host, self.port))

    def start(self):
        self._running = self.ON

    def stop(self):
        self._running = self.OFF

    @abstractclassmethod
    def run(self):
        raise NotImplementedError("Método não implementado")
