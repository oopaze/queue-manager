from server.shared.connection import BaseConnection


class MockedConnection(BaseConnection):
    def run(self):
        ...
