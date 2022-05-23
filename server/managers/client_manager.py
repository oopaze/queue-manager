from json import loads
from typing import List, Literal, TypedDict

from server.utils.get_moment import get_moment
from shared.contracts import MessageContract
from shared.socket import Socket


class RawMessageContract(TypedDict):
    content: str
    moment: str


class ClientContract(TypedDict):
    name: str
    type: Literal["client", "watcher"]
    messages: List[RawMessageContract]


class ClientManager:
    clients: ClientContract = {}
    amount_of_client = 0

    def submit(self, encoded_message, address) -> MessageContract:
        client = self.get_or_register_client(address[0])
        message = self.decode_message(encoded_message)
        client["messages"].append({"content": message, "moment": get_moment()})
        return message

    def decode_message(self, message):
        return loads(message.decode())

    def get_or_register_client(self, address: str) -> ClientContract:
        if address in self.clients.keys():
            return self.clients[address]

        self.amount_of_client += 1
        self.clients[address] = {
            "name": f"Guiche {self.amount_of_client}",
            "type": "client", 
            "messages": [],
        }

        return self.clients[address]
