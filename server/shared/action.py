from abc import ABCMeta, abstractmethod
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
        name: str = "create_ticket",
        callback: Callable = None,
    ):
        super().__init__(name, master, callback)

    def action(self, is_preferential: bool = False):
        return self.master.queue_manager.add(is_preferential=is_preferential)


class NextTicketAction(Action):
    name = "next_ticket"

    def __init__(
        self,
        master: Server,
        name: str = "next_ticket",
        callback: Callable = None,
    ):
        super().__init__(name, master, callback)

    def action(self):
        try:
            return self.master.queue_manager.next()
        except EmptyQueueException as e:
            return str(e)
