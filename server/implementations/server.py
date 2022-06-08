from socket import AF_INET, SOCK_STREAM, gethostbyname, gethostname, socket
from threading import Thread

from server.shared.runner import Runner
from server.managers.queue_manager import QueueManager


class Server(socket, Runner):
    MAX_CLIENTS = 10
    PORT = 50000
    HOST = gethostbyname(gethostname())

    def __init__(self, family=AF_INET, type=SOCK_STREAM, *args, **kwargs):
        from server.managers.client_manager import ClientManager

        super().__init__(family, type, *args, **kwargs)

        self._running = self.OFF
        self.queue_manager = QueueManager()
        self.client_manager = ClientManager()

    def bind(self) -> None:
        address = (self.HOST, self.PORT)
        print(f"Iniciando servidor: {self.HOST}:{self.PORT}")
        return super().bind(address)

    def listen(self) -> None:
        print(f"Ouvindo até {self.MAX_CLIENTS} clientes simultaneos")
        return super().listen(self.MAX_CLIENTS)

    def close(self):
        self.client_manager.stop_all_clients()
        print("Encerrando servidor... \nbye, bye!")
        super().close()

    def run(self):
        self.start()
        self.bind()
        self.listen()

        print("Aplicação pronta para conexão\n")
        while self.running:
            self.routine()

        self.close()

    def routine(self):
        client, address = self.accept()
        print(f"Novo cliente conectado: {address[0]}:{address[1]}")

        connection = self.get_connection(server=self, client=client)
        connection_thread = Thread(target=connection.run)
        connection_thread.start()

        self.client_manager.add_client(connection, connection_thread)
        self.client_manager.clean_dead_clients()

    def get_connection(self, *args, **kwargs) -> bool:
        from server.implementations.tsta_connection import TSTAConnection

        return TSTAConnection(*args, **kwargs)
