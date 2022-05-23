import queue
from server.managers.client_manager import ClientManager
from server.managers.queue_manager import QueueManager
from shared.socket import Socket


class Server(Socket):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client_manager = ClientManager()
        self.queue_manager = QueueManager()

        self.actions = {
            "next": self.propagate,
            "add": self.queue_manager.register_queue_item,
            "register_as_watcher": self.client_manager.register_as_watcher,
            "reset": self.queue_manager.reset_queue
        }

    def error_action(self, *args, **kwargs):
        return "Ação inesperada"

    def propagate(self):
        queue_item = self.queue_manager.get_next_queue_item()
        send_message = self.format_message(queue_item)

        clients = self.client_manager.get_all_watchers()

        for client in clients:
            self.sendto(send_message, client["address"])

    def format_message(self, message: str):
        return f"{'message': {message}}".encode()

    def run(self):
        self.start()

        while self.running:
            message, address = self.recvfrom(2048)
            data = self.client_manager.submit(message, address)

            action = self.actions.get(data["action"], self.error_action)
            send_message = action(*data["args"], **data["kwargs"])


            send_message = self.format_message("Ok")
            self.sendto(send_message, address)
