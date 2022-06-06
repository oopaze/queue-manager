from server.implementations.server import Server


class MockedServer(Server):
    def accept(self) -> str:
        return "Client 1", ""
