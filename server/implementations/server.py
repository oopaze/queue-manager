from socket import AF_INET, SOCK_STREAM, gethostbyname, gethostname, socket

from server.shared.runner import Runner
from server.managers.queue_manager import QueueManager


class Server(socket, Runner):
    MAX_CLIENTS = 10
    PORT = 50000
    HOST = gethostbyname(gethostname())

    def __init__(self, family=AF_INET, type=SOCK_STREAM, *args, **kwargs):
        super().__init__(family, type, *args, **kwargs)

        self._running = self.OFF
        self.queue_manager = QueueManager()

    def bind(self) -> None:
        address = (self.HOST, self.PORT)
        return super().bind(address)

    def listen(self) -> None:
        return super().listen(self.MAX_CLIENTS)

    def run(self):
        self.start()
        self.bind()
        self.listen()

        while self.running:
            client, address = self.accept()

            print(f"Cliente conectado: {client}")

        self.close()
