from json import loads
from typing import List, TypedDict

from server.utils.get_moment import get_moment


class MessageContract(TypedDict):
    actions: str  # Literal["actions_name"]


class RawMessageContract(TypedDict):
    content: str
    moment: str


class ClientContract(TypedDict):
    name: str
    messages: List[RawMessageContract]


class ClientManager:
    clients: ClientContract = {}
    amount_of_client = 0

    def submit(self, encoded_message, address):
        client = self.get_or_register_client(address[0])
        message = self.decode_message(encoded_message)
        client["messages"].append({"content": message, "moment": get_moment()})

        send_message = "Ok"

        return send_message.encode()

    def decode_message(self, message):
        return loads(message.decode())

    def get_or_register_client(self, address: str) -> ClientContract:
        if address in self.clients.keys():
            return self.clients[address]

        self.amount_of_client += 1
        self.clients[address] = {
            "name": f"Guiche {self.amount_of_client}",
            "messages": [],
        }

        return self.clients[address]
