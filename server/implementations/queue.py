from queue import Empty, Queue as DefaultQueue
from typing import Any, List

from server.exceptions import EmptyQueueException


class Queue(DefaultQueue):
    MAX_SIZE = 1000

    def __init__(self, *args, prefix: str, **kwargs):
        super().__init__(*args, maxsize=self.MAX_SIZE, **kwargs)

        if not isinstance(prefix, str):
            raise TypeError("prefix deve ser uma string")

        self.prefix = prefix
        self.counter = 0
        self.amount_tickets_called = 0

    def generate(self):
        ticket = f"{self.prefix}{self.counter}"
        return ticket

    def add(self):
        self.counter += 1
        ticket = self.generate()
        self.put(ticket)
        return ticket

    def next(self):
        try:
            next_ticket = self.get(block=False)
            self.amount_tickets_called += 1
            return next_ticket
        except Empty:
            raise EmptyQueueException()

    @staticmethod
    def from_array(array: List[Any], prefix: str = "N"):
        queue = Queue(prefix=prefix)

        for item in array:
            queue.put(item)

        return queue
