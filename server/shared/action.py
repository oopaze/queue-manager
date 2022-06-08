from abc import ABCMeta, abstractmethod
from threading import Thread
from typing import Callable

from server.implementations.server import Server
from server.exceptions import EmptyQueueException


class Action(metaclass=ABCMeta):
    name = None

    def __init__(self, name: str, master: Server, callback: Callable = None):
        self.name = name
        self.callback = callback

        if not isinstance(master, Server):
            raise TypeError("master deve ser uma instancia de server")

        self.master = master

    def run(self, *args, **kwargs):
        action_return = self.action(*args, **kwargs)

        if self.callback is not None:
            self.callback(action_return)

        return action_return

    @abstractmethod
    def action(self):
        ...


class InvalidAction(Action):
    def __init__(
        self,
        master: Server,
        name: str = "invalid",
        callback: Callable = None,
    ):
        super().__init__(name, master, callback)

    def action(self):
        return "Ação inválida"


class CreateTicketAction(Action):
    name = "create_ticket"

    def __init__(
        self,
        master: Server,
        callback: Callable = None,
    ):
        super().__init__(self.name, master, callback)

    def action(self, is_preferential: bool = False):
        return self.master.queue_manager.add(is_preferential=is_preferential)


class NextTicketAction(Action):
    name = "next_ticket"

    def __init__(
        self,
        master: Server,
        callback: Callable = None,
    ):
        super().__init__(self.name, master, callback)

    def action(self):
        try:
            return self.master.queue_manager.next()
        except EmptyQueueException as e:
            return str(e)


class TransformIntoTVAction(Action):
    name = "transform_tv_connection"

    def __init__(
        self,
        master: Server,
        connection,
        callback: Callable = None,
    ):
        super().__init__(self.name, master, callback)
        self.connection = connection

    def action(self):
        from server.implementations.tv_connection import TVConnection

        self.connection.stop()

        tv_connection = TVConnection(self.master, self.connection.client)
        connection_thread = Thread(target=tv_connection.run)
        connection_thread.start()
        self.master.client_manager.add_client(tv_connection, connection_thread)
        self.master.client_manager.clean_dead_clients()
