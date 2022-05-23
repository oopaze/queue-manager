from server.managers.client_manager import ClientManager
from shared.socket import Socket


class Server(Socket):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client_manager = ClientManager()

    def run(self):
        self.start()

        while self.running:
            message, address = self.recvfrom(2048)
            message = self.client_manager.submit(message, address)
            send_message = "Ok"
            self.sendto(send_message.encode(), address)
