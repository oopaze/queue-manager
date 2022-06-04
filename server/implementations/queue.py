from server.exceptions import EmptyQueueException


class Queue:
    def __init__(self, prefix: str):
        self.prefix = prefix
        self.counter = 0
        self.tickets = []

    def generate(self):
        ticket = f"{self.prefix}{self.counter}"
        return ticket

    def add(self):
        self.counter += 1
        ticket = self.generate()
        self.tickets.append(ticket)
        return ticket

    def next(self):
        try:
            return self.tickets.pop(0)
        except IndexError:
            raise EmptyQueueException()
