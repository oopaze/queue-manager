from socket import socket

from server.managers.queue_manager import QueueManager
from server.implementations.server import Server
from server.shared.runner import Runner


class BaseConnection(Runner):
    def __init__(self, server: Server, client: socket):
        super().__init__()
        self._queue_manager = None
        self.server = server
        self.client = client

    @property
    def queue_manager(self):
        return self._queue_manager

    @queue_manager.setter
    def queue_manager(self, queue_manager: QueueManager):
        if not isinstance(queue_manager, QueueManager):
            raise TypeError("queue_manager deve ser uma instância de QueueManager")

        self._queue_manager = queue_manager
