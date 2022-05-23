import queue

from server.exceptions import EmptyQueueError
from server.implementations.server import Server


class QueueManager:
    PREFERENCIAL_PREFIX = "C"

    def __init__(self, server: Server):
        self.queue = []
        self.passed_queue = []
        self.queue_counter = 1000

    def get_queue(self):
        return self.queue

    def register_queue_item(self, is_preferencial: bool = False):
        self.queue_counter += 1

        queue_item = f"{self.queue_counter}"

        if is_preferencial:
            queue_item = self.PREFERENCIAL_PREFIX + queue_item

        self.queue.append(queue_item)

        return queue_item

    def get_next_queue_item(self):
        if len(self.queue) == 0:
            raise EmptyQueueError("A fila está vazia")

        queue_item = self.queue.pop()
        self.passed_queue.append(queue_item)
        return queue_item

    def reset_queue(self):
        self.queue = []
        self.passed_queue = []

        return "'Fila resetada com sucesso'"
