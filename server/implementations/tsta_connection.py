from json import JSONDecodeError
from typing import Dict

from server.managers.message_manager import MessageManager
from server.shared.connection import BaseConnection
from server.shared.action import (
    CreateTicketAction,
    InvalidAction,
    NextTicketAction,
    Action,
)


class TSTAConnection(BaseConnection):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.message_manager = MessageManager()
        self.actions: Dict[str, Action] = {
            CreateTicketAction.name: CreateTicketAction(self.server),
            NextTicketAction.name: NextTicketAction(self.server),
        }

        self.invalid_action = InvalidAction(self.server)

    def run(self):
        self.start()

        while self.running:
            encoded_message = self.client.recv(2048)

            if not encoded_message:
                continue

            try:
                message = self.message_manager.decode(encoded_message)
                action_instance = self.actions.get(
                    message.get("action", ""), self.invalid_action
                )
                args = message["args"]
                kwargs = message["kwargs"]

            except JSONDecodeError:
                action_instance = self.invalid_action
                args, kwargs = [], {}

            send_message = action_instance.run(*args, **kwargs)

            self.client.send(self.message_manager.encode(send_message))

        self.client.close()
