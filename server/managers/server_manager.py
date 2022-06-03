from threading import Thread

from server.implementations.server import Server
from server.exceptions import ServerError
from shared.widgets.screen import Screen


class ServerManager:
    server_thread = None
    server_instance = None

    @classmethod
    def start_server(cls, screen: Screen):
        if cls.server_instance is None:
            cls.server_instance = Server(screen=screen)

        cls.server_thread = Thread(target=cls.server_instance.run)
        cls.server_thread.start()

    @classmethod
    def stop_server(cls):
        if cls.server_instance:
            cls.server_instance.stop()
            cls.server_instance = None
        else:
            raise ServerError("Nenhum servidor rodando no momento")
