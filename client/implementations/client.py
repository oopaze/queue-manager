from shared.socket import Socket


class Client(Socket):
    def run(self):
        self.start()

        while self.running:
            ...
