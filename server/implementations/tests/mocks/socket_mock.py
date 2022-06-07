from socket import SOL_SOCKET, SO_REUSEADDR
from server.implementations.server import Server


class MockedServer(Server):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    def accept(self) -> str:
        return "Client 1", ("", "")
