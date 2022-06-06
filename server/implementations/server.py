from socket import AF_INET, SOCK_STREAM, socket
from server.shared.runner import Runner


class Server(socket, Runner):
    def __init__(self, family=AF_INET, type=SOCK_STREAM, *args, **kwargs):
        super().__init__(family, type, *args, **kwargs)

        self._running = self.OFF

    def run(self):
        self.start()

        while self.running:
            client, address = self.accept()

            print(f"Cliente conectado: {client}")
