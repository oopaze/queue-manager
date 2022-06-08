from threading import Lock, Thread
from typing import TypedDict, List, Union

from server.implementations.tsta_connection import TSTAConnection
from server.implementations.tv_connection import TVConnection


class ClientContract(TypedDict):
    thread: Thread
    connection: Union[TSTAConnection, TVConnection]


class ClientManager:
    def __init__(self) -> None:
        self.clients: List[ClientContract] = []
        self.lock = Lock()

    def get_clients(
        self, type=(TSTAConnection, TVConnection)
    ) -> List[ClientContract]:
        self.lock.acquire()
        clients = list(
            filter(
                lambda client: isinstance(client["connection"], type), self.clients
            )
        )

        self.lock.release()

        return clients

    def add_client(self, connection, thread: Thread):
        if not isinstance(connection, (TVConnection, TSTAConnection)):
            raise TypeError(
                "connection deve ser uma implementação TV ou TSTA connection"
            )

        self.lock.acquire()
        self.clients.append({"connection": connection, "thread": thread})
        self.lock.release()

    def clean_dead_clients(self):
        clients = []

        self.lock.acquire()

        for idx, client in enumerate(self.clients):
            client_thread = client["thread"]

            if not client_thread.is_alive():
                ...
            else:
                clients.append(self.clients[idx])

        self.clients = clients
        self.lock.release()

    def stop_all_clients(self):
        self.lock.acquire()

        for client in self.clients:
            client["connection"].stop()

        self.clients = []
        self.lock.release()
