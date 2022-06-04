"""
Para cada 2 senhas normais, 1 preferencial é chamada

"""


class QueueManager:
    queue_number = 1000

    def __init__(self):
        self.normal_tickets = []
        self.preferential_tickets = []
        self.history = []
        self.amount_tickets_called = 1

    def next(self):
        is_third_ticket = self.amount_tickets_called % 3 == 0
        there_is_preferential = len(self.preferential_tickets) > 0

        if is_third_ticket and there_is_preferential:
            next_ticket = self.preferential_tickets.pop(0)
        else:
            next_ticket = self.normal_tickets.pop(0)

        self.amount_tickets_called += 1

        return next_ticket

    def add(self, is_preferential: bool = False):
        ticket_number = self.queue_number = self.queue_number + 1

        if is_preferential:
            self.preferential_tickets.append(ticket_number)
        else:
            self.normal_tickets.append(ticket_number)

        return f'Ticket "{ticket_number}" adicionado com sucesso.'
