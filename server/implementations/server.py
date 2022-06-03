import json

from server.exceptions import EmptyQueueError
from server.managers.client_manager import ClientContract, ClientManager
from server.managers.queue_manager import QueueManager
from shared.socket import Socket


class Server(Socket):
    last_client: ClientContract = None
    item_template = "Senha: {queue_item}\nGuiche: {guiche}"

    def __init__(self, screen, *args, **kwargs):
        self.screen = screen
        super().__init__(*args, **kwargs)
        self.client_manager = ClientManager()
        self.queue_manager = QueueManager()

        self.actions = {
            "next": self.next_item,
            "add": self.queue_manager.add,
            "reset": self.queue_manager.reset,
            "get": self.queue_manager.get,
        }

    def error_action(self, *args, **kwargs):
        return "Ação inesperada"

    def next_item(self):
        try:
            queue_item = self.queue_manager.next()
            message = self.item_template.format(
                queue_item=queue_item, guiche=self.last_client["name"]
            )
            self.screen.update_label_item(message)
            return message
        except EmptyQueueError as err:
            return str(err)

    def format_message(self, message: str):
        message = json.dumps({"message": message}, ensure_ascii=True, skipkeys=True)
        return message.encode("utf-8")

    def run(self):
        self.start()

        while self.running:
            message, address = self.recvfrom(2048)
            data = self.client_manager.submit(message, address)
            print(f"New connection from {address[0]}:{address[1]}")
            self.last_client = self.client_manager.get_or_register_client(
                address[0]
            )

            action = self.actions.get(data["action"], self.error_action)
            send_message = action(*data["args"], **data["kwargs"])

            send_message = self.format_message(send_message)
            self.sendto(send_message, address)

        self.close()
