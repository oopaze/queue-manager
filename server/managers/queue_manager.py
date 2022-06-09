from threading import Lock
from server.exceptions import EmptyQueueException
from server.implementations.queue import Queue


class QueueManager:
    def __init__(self):
        self.normal_queue = Queue(prefix="N")
        self.preferential_queue = Queue(prefix="P")
        self.last_ticket_called = None

    def check_preferential_time(self):
        n_ticket_amount = self.normal_queue.amount_tickets_called + 1
        p_ticket_amount = self.preferential_queue.amount_tickets_called

        is_third_ticket = (n_ticket_amount + p_ticket_amount) % 3 == 0
        return is_third_ticket or self.normal_queue.empty()

    def next(self):
        if self.check_preferential_time():
            try:
                next_ticket = self.preferential_queue.next()
            except EmptyQueueException:
                next_ticket = self.normal_queue.next()
        else:
            next_ticket = self.normal_queue.next()
            
        return next_ticket

    def add(self, is_preferential: bool = False):
        if is_preferential:
            ticket = self.preferential_queue.add()
        else:
            ticket = self.normal_queue.add()

        return ticket
