from json import JSONDecodeError
from typing import Dict
from server.implementations.tv_connection import TVConnection

from server.managers.message_manager import MessageManager
from server.shared import get_moment
from server.shared.connection import BaseConnection
from server.shared.action import (
    CreateTicketAction,
    InvalidAction,
    NextTicketAction,
    Action,
    TransformIntoTVAction,
)


class TSTAConnection(BaseConnection):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.message_manager = MessageManager()
        self.actions: Dict[str, Action] = {
            CreateTicketAction.name: CreateTicketAction(self.server),
            NextTicketAction.name: NextTicketAction(self.server, self.propagate),
            TransformIntoTVAction.name: TransformIntoTVAction(self.server, self),
        }

        self.invalid_action = InvalidAction(self.server)
        self.host, self.port = self.client.getpeername()

    def propagate(self, ticket):
        tv_clients = self.server.client_manager.get_clients(type=TVConnection)

        for client in tv_clients:
            client["connection"].add_new_message(ticket)

    def routine(self):
        try:
            encoded_message = self.client.recv(2048)
        except ConnectionResetError:
            self.stop()
            self.client.close()
            return

        if not encoded_message:
            return

        try:
            message = self.message_manager.decode(encoded_message)
            action_instance = self.actions.get(
                message.get("action", ""), self.invalid_action
            )
            args = message["args"]
            kwargs = message["kwargs"]

        except (JSONDecodeError, UnicodeDecodeError):
            action_instance = self.invalid_action
            args, kwargs = [], {}

        print(f"[CLIENTE:{self.port}] - {get_moment()} - {action_instance.name}")
        send_message = action_instance.run(*args, **kwargs)

        self.client.send(self.message_manager.encode(send_message))
        print(
            f"TSTA - [CLIENT:{self.port}] - {get_moment()} - {send_message or 'NO ANSWER'}"
        )
