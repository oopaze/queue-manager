from typing import Callable

from client.contracts import HomeButtonContract
from client.defaults import APP_SIZE, BLUE, LIGHTBLUE
from client.managers.event_manager import EventManager
from client.implementations.app import ClientApp as App
from shared.widgets.screen import Screen
from shared.widgets.button import Button


class Home(Screen):
    _screen_name = "home"
    buttons = []
    commands = {}
    BUTTONS: HomeButtonContract = [
        {"text": "Próximo", "name": "next"},
        {"text": "Ver Senhas", "name": "get"},
        {"text": "Adicionar Senha", "name": "add"},
        {"text": "Mostrar Senha", "name": "show"},
        {"text": "Resetar Fila", "name": "reset"},
    ]

    def __init__(self, *args, **kwargs):
        self.app: App = args[0]
        self.event_manager: EventManager = self.app.client.event_manager

        self.commands = {"next": self.next, "reset": self.reset, "show": self.show}

        kwargs.update({"width": APP_SIZE[0], "height": APP_SIZE[1]})
        super().__init__(*args, **kwargs)

    def get_command(self, name: str) -> Callable:
        return self.commands.get(name, lambda: print("tapped"))

    def build(self):
        for i, button_kwargs in enumerate(self.BUTTONS):
            command = self.get_command(button_kwargs["name"])
            button = Button(
                self,
                fg=BLUE,
                bg=LIGHTBLUE,
                text=button_kwargs["text"],
                command=command,
            )
            button.place(x=50, y=i * 60 + 80)
            self.buttons.append(button)

    def next(self):
        message = {"action": "next"}
        encoded_message = self.app.client.encode_message(message)
        return self.event_manager.add(
            {
                "message": encoded_message,
                "action": self.app.screens["show_password"].update_password_time,
            },
        )

    def reset(self):
        message = {"action": "reset"}
        encoded_message = self.app.client.encode_message(message)
        return self.event_manager.add({"message": encoded_message})

    def show(self):
        self.next()
        self.switch_screen("show_password")
