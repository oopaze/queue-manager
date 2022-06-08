from queue import Empty, Queue as SyncronizedQueue
from typing import Callable

from server.shared.connection import BaseConnection


class TVConnection(BaseConnection):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.events: "SyncronizedQueue[Callable]" = SyncronizedQueue(20)

    def add_new_event(self, event: Callable):
        if not callable(event):
            raise TypeError("Evento deve ser um chamável")

        self.events.put(event)

    def routine(self, timeout=5):
        try:
            event = self.events.get(timeout=timeout)
            event()
        except Empty:
            return
