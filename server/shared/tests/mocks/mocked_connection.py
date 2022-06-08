from server.implementations.server import Server
from server.shared.connection import BaseConnection


class MockedConnection(BaseConnection):
    def __init__(self, server=Server(), client=""):
        super().__init__(server, client)

    def routine(self):
        ...
