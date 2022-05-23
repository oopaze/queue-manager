from calendar import c
from enum import Enum
from typing import Any, Dict, Literal
from shared.widgets.button import Button
from shared.widgets.screen import Screen
from server.defaults import APP_SIZE, LIGHTGREEN, LIGHTRED, RED, GREEN


class Home(Screen):
    _screen_name = "home"

    def __init__(
        self, *args, width: int = APP_SIZE[0], height: int = APP_SIZE[1], **kwargs
    ):
        kwargs.update({"width": width, "height": height})
        super().__init__(*args, **kwargs)

    def build(self):
        self.button = Button(
            self,
            text="Iniciar servidor",
            fg=GREEN,
            bg=LIGHTGREEN,
            command=self.start_server,
        )
        self.button.place(x=50, y=180)

    def start_server(self):
        self.button.configure(
            text="Parar servidor", fg=RED, bg=LIGHTRED, command=self.stop_server
        )

    def stop_server(self):
        self.button.configure(
            text="Iniciar servidor",
            fg=GREEN,
            bg=LIGHTGREEN,
            command=self.start_server,
        )
