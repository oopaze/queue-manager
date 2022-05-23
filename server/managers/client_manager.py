from typing import List, TypedDict

from server.managers.message_manager import MessageContract


class ClientContract(TypedDict):
    name: str
    messages: List[MessageContract]


class ClientManager:
    clients: ClientContract = {}
    amount_of_client = 0

    def register_client(self, address: str):
        self.amount_of_client += 1
        self.clients[address] = {
            "name": f"Guiche {self.amount_of_client}",
            "messages": []
        }

    def get_client_name(self, address: str) -> str:
        return self.clients[address]["name"]
