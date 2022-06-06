from queue import Empty, Queue as DefaultQueue
from typing import Any, List

from server.exceptions import EmptyQueueException


class Queue(DefaultQueue):
    def __init__(self, *args, prefix: str, **kwargs):
        super().__init__(*args, **kwargs)
        self.prefix = prefix
        self.counter = 0

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
            return self.get(block=False)
        except Empty:
            raise EmptyQueueException()

    @staticmethod
    def from_array(array: List[Any], prefix: str = "N"):
        queue = Queue(prefix=prefix)

        for item in array:
            queue.put(item)

        return queue
