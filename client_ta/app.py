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
        super().__init__()
        self.client_thread.start()
        self.geometry(f"300x300")
        self.resizable(0, 0)
        self.title("Cliente TA - v1.0")
        self.build_widgets()

    def build_widgets(self):
        self.ticket = Label(self, text="Olá", font=("Arial", 64), fg="#00304d")
        self.empty = Label(self, text="Bom trabalho!", fg="#53875f")
        self.next = Button(
            self,
            text="Próximo",
            fg="#0f5763",
            bg="#d1ecf1",
            command=self.next_command,
        )

        self.ticket.place(x=50, y=35, width=200)
        self.empty.place(x=0, y=160, width=300)
        self.next.place(x=50, y=200, width=200, height=40)

    def update_ticket(self, message: Dict[str, Any]):
        next_ticket = message.get("message", None)

        if next_ticket == "A lista está vazia" or not next_ticket:
            self.empty.configure(text=next_ticket, fg="#721c24")
        else:
            self.ticket.configure(text=next_ticket)
            self.empty.configure(
                text="Você está atendendo a senha acima", fg="#53875f"
            )

    def next_command(self):
        encoded_message = self.NEXT_TICKET_MESSAGE.encode("utf8")
        self.client.send_message(encoded_message, self.update_ticket)

    def run(self):
        self.mainloop()
