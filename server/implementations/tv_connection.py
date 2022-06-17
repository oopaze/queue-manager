from queue import Empty, Queue as SyncronizedQueue

from server.managers.message_manager import MessageManager
from server.shared.connection import BaseConnection
from server.shared import get_moment


class TVConnection(BaseConnection):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.messages: "SyncronizedQueue[str]" = SyncronizedQueue(20)
        self.message_manager = MessageManager()
        self.host, self.port = self.client.getpeername()

    def add_new_message(self, message: str):
        self.messages.put(message)

    def routine(self, timeout=5):
        try:
            message = self.messages.get(timeout=timeout)
            encoded_message = self.message_manager.encode(message)
            self.client.send(encoded_message)
            print(f"TV - [CLIENT:{self.port}] - {get_moment()} - {message or 'NO ANSWER'}")
        except Empty:
            ...
