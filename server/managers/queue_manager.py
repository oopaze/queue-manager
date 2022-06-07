"""
Para cada 2 senhas normais, 1 preferencial é chamada

"""


from server.exceptions import EmptyQueueException
from server.implementations.queue import Queue


class QueueManager:
    def __init__(self):
        self.normal_queue = Queue(prefix="N")
        self.preferential_queue = Queue(prefix="P")
        self.amount_tickets_called = 0
        self.last_ticket_called = None

    def check_preferential_time(self):
        is_third_ticket = (self.amount_tickets_called + 1) % 3 == 0
        return is_third_ticket or self.normal_queue.empty()

    def next(self):
        if self.check_preferential_time():
            try:
                next_ticket = self.preferential_queue.next()
            except EmptyQueueException:
                next_ticket = self.normal_queue.next()
        else:
            next_ticket = self.normal_queue.next()

        self.last_ticket_called = next_ticket
        self.amount_tickets_called += 1
        return next_ticket

    def add(self, is_preferential: bool = False):
        if is_preferential:
            ticket = self.preferential_queue.add()
        else:
            ticket = self.normal_queue.add()

        return ticket
