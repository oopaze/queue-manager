from shared.widgets.button import Button
from shared.widgets.screen import Screen
from server.defaults import APP_SIZE, LIGHTRED, RED

from server.managers.server_manager import ServerManager
from server.implementations.server import server_instance


class Stop(Screen):
    _screen_name = "stop"

    def __init__(
        self, *args, width: int = APP_SIZE[0], height: int = APP_SIZE[1], **kwargs
    ):
        kwargs.update({"width": width, "height": height})
        super().__init__(*args, **kwargs)

    def build(self):
        self.button = Button(
            self,
            text="Parar servidor",
            fg=RED,
            bg=LIGHTRED,
            command=self.stop_server,
        )
        self.button.place(x=50, y=180)

    def stop_server(self):
        self.switch_screen('start')
        ServerManager.stop_server()
