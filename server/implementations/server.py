from socket import AF_INET, SOCK_DGRAM, socket, gethostname, gethostbyname

from server.managers.client_manager import ClientManager


server_instance = None
server_thread = None


class Server(socket):
    ON = "on"
    OFF = "off"

    host = gethostbyname(gethostname())
    port = 5000
    _running = OFF

    client_manager = ClientManager()

    def __init__(self, *args, **kwargs):
        kwargs.update({"family": AF_INET, "type": SOCK_DGRAM})
        super().__init__(*args, **kwargs)
        self.bind()

    @property
    def running(self):
        return self._running == self.ON

    def bind(self):
        super().bind((self.host, self.port))

    def start(self):
        self._running = self.ON

    def stop(self):
        self._running = self.OFF

    def run(self):
        self.start()

        while self.running:
            message, address = self.recvfrom(2048)
            send_message = self.client_manager.submit(message, address)
            self.sendto(send_message, address)
