from typing import Callable
from client.contracts import HomeButtonContract
from client.defaults import APP_SIZE, BLUE, GREEN, LIGHTBLUE, LIGHTGREEN
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
        {"text": "Resetar Fila", "name": "reset"},
    ]

    def __init__(
        self, *args, width: int = APP_SIZE[0], height: int = APP_SIZE[1], **kwargs
    ):
        kwargs.update({"width": width, "height": height})
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
            button.place(x=50, y=i * 60 + 100)
