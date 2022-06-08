from functools import partial
from threading import Thread
from tkinter import Tk, Button, Label
from typing import Any, Dict

from client_ta.client import Client


class App(Tk):
    client = Client()
    client_thread = Thread(target=client.connect)

    PREFERENTIAL_TEMPLATE = """{
        "action": "create_ticket",
        "kwargs": {
            "is_preferential": true
        }
    }"""

    NORMAL_TICKET_TEMPLATE = """{
        "action": "create_ticket"
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
        self.empty = Label(
            self, text="Gere sua senha apertando\nnos botões abaixo!", fg="#53875f"
        )

        self.normal = Button(
            self,
            text="Normal",
            fg="#0f5763",
            bg="#d1ecf1",
            command=self.get_ticket,
        )

        self.preferential = Button(
            self,
            text="Preferencial",
            fg="#0f5763",
            bg="#d1ecf1",
            command=partial(self.get_ticket, ["P"]),
        )

        self.ok = Button(
            self, text="Ok", fg="#53875f", bg="#d4edda", command=self.confirm_ticket
        )

        self.ticket.place(x=50, y=35, width=200)
        self.empty.place(x=0, y=160, width=300)

        self.normal.place(x=150, y=210, width=125, height=40)
        self.preferential.place(x=25, y=210, width=125, height=40)

    def update_ticket(self, message: Dict[str, Any]):
        generated_ticket = message.get("message", None)
        self.ticket.configure(text=generated_ticket)
        self.empty.configure(text="Essa é a sua senha")

        self.normal.place_forget()
        self.preferential.place_forget()
        self.ok.place(x=50, y=215, width=200, height=40)

    def confirm_ticket(self):
        self.ticket.configure(text="Olá")
        self.empty.configure(text="Gere sua senha apertando\nnos botões abaixo!")
        self.normal.place(x=150, y=210, width=125, height=40)
        self.preferential.place(x=25, y=210, width=125, height=40)
        self.ok.place_forget()

    def get_ticket(self, ticket_type: str = "N"):
        message_template = (
            self.NORMAL_TICKET_TEMPLATE
            if ticket_type == "N"
            else self.PREFERENTIAL_TEMPLATE
        )
        encoded_message = message_template.encode("utf8")
        self.client.send_message(encoded_message, self.update_ticket)

    def run(self):
        self.mainloop()
