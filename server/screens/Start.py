from shared.widgets.button import Button
from shared.widgets.screen import Screen
from server.defaults import APP_SIZE, LIGHTGREEN, GREEN
from server.managers.server_manager import ServerManager


class Start(Screen):
    _screen_name = "start"

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
        self.button.place(x=50, y=100)

    def start_server(self):
        self.switch_screen('stop')
        ServerManager.start_server()
