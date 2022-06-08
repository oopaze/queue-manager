from threading import Thread
from tkinter import Tk, Button, Label
from typing import Any, Dict

from client_tv.client import Client


class App(Tk):
    def __init__(self) -> None:
        self.client = Client(self.update_ticket)
        self.client_thread = Thread(target=self.client.run)
        self.client_thread.start()

        super().__init__()
        self.geometry(f"300x300")
        self.resizable(0, 0)
        self.title("Cliente TA - v1.0")
        self.build_widgets()

    def build_widgets(self):
        self.ticket = Label(self, text="Olá", font=("Arial", 96), fg="#00304d")
        self.message = Label(
            self,
            font=("Arial", 18),
            text="Logo, logo chamaremos\n a sua senha!",
            fg="#53875f",
        )

        self.ticket.place(x=0, y=30, width=300)
        self.message.place(x=0, y=200, width=300)

    def update_ticket(self, ticket: str):
        self.ticket.configure(text=ticket)
        self.message.configure(text=f"{ticket} é a sua vez\n de ser atendido")

    def run(self):
        self.mainloop()
