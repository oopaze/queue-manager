from threading import Thread
from tkinter import Tk, Button, Label
from typing import Any, Dict

from client_ta.client import Client


class App(Tk):
    client = Client()
    client_thread = Thread(target=client.connect)

    NEXT_TICKET_MESSAGE = """{
        "action": "next_ticket"
    }"""

    def __init__(self) -> None:
        super().__init__("Client TA")
        self.client_thread.start()
        self.geometry(f"300x300")
        self.resizable(0, 0)
        self.title("Cliente TA - v1.0")
        self.build_widgets()

    def build_widgets(self):
        self.ticket = Label(self, text="")
        self.empty = Label(self, text="Olá, seja bem vindo!")
        self.next = Button(self, text="Próximo", command=self.next_command)

        self.ticket.place(x=0, y=0)
        self.empty.place(x=0, y=50)
        self.next.place(x=0, y=100)

    def update_ticket(self, message: Dict[str, Any]):
        next_ticket = message.get("message", None)

        if next_ticket == "A lista está vazia" or not next_ticket:
            self.empty.configure(text=next_ticket)
        else:
            self.ticket.configure(text=next_ticket)

    def next_command(self):
        encoded_message = self.NEXT_TICKET_MESSAGE.encode("utf8")
        self.client.send_message(encoded_message, self.update_ticket)

    def run(self):
        self.mainloop()
