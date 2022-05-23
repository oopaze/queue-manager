from json import loads
from typing import Dict, List, Literal, TypedDict
from server.exceptions import ClientNotFoundError

from server.utils.get_moment import get_moment
from shared.contracts import MessageContract


class RawMessageContract(TypedDict):
    content: str
    moment: str


class ClientContract(TypedDict):
    name: str
    address: str
    type: Literal["client", "watcher"]
    messages: List[RawMessageContract]


class ClientManager:
    clients: Dict[str, ClientContract] = {}
    amount_of_client = 0

    def submit(self, encoded_message, address) -> MessageContract:
        client = self.get_or_register_client(address[0])
        message = self.decode_message(encoded_message)
        client["messages"].append({"content": message, "moment": get_moment()})
        return message

    def register_as_watcher(self, address):
        client = self.get_or_register_client.get(address)
        client["type"] = "watcher"

        return "Cliente registrado com sucesso"

    def decode_message(self, message):
        data: MessageContract = loads(message.decode())

        args_was_passed = not isinstance(data.get("args", None), list)
        if args_was_passed:
            data["args"] = []

        kwargs_was_passed = not isinstance(data.get("kwargs", None), dict)
        if kwargs_was_passed:
            data["kwargs"] = {}
        
        return data

    def get_all_watchers(self) -> List[ClientContract]:
        return list(filter(lambda item: item["type"] == "watcher", self.clients))

    def get_or_register_client(self, address: str) -> ClientContract:
        if address in self.clients.keys():
            return self.clients[address]

        self.amount_of_client += 1
        self.clients[address] = {
            "name": f"Guiche {self.amount_of_client}",
            "address": address,
            "type": "client", 
            "messages": [],
        }

        return self.clients[address]
