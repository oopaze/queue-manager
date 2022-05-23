from typing import TypedDict


class MessageContract(TypedDict):
    actions: str # Literal["actions_name"]


class MessageManager:
    def decode_message(self, message):
        message = message.decode()
        

