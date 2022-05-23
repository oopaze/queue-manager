from socket import AF_INET, SOCK_DGRAM, socket, gethostname, gethostbyname


server_instance = None
server_thread = None


class Server(socket):
    ON = 'on'
    OFF = 'off'

    host = gethostbyname(gethostname())
    port = 5000
    _running = OFF

    def __init__(self, *args, family: int = AF_INET, type: int = SOCK_DGRAM, **kwargs):
        kwargs.update({"family": family, "type": type})
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
        self.close()

    def run(self):
        self.start()

        while self.running:
            body, address = self.recvfrom(2048)
            body = body.decode()


