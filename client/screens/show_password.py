from threading import Thread

from client.defaults import APP_SIZE, GREEN, LIGHTGREEN
from client.implementations.app import ClientApp
from shared.widgets.screen import Screen
from shared.widgets.label import Label
from shared.widgets.button import Button


class ShowPassword(Screen):
    _screen_name = "show_password"

    def __init__(self, *args, **kwargs):
        kwargs.update({"width": 300, "height": 300})
        super().__init__(*args, **kwargs)
        self.app: ClientApp = self.master
        self.update_thread = Thread(target=self.update_password_time)

    def place(self, *args, **kwargs):
        self.app.set_base_config((300, 300))
        return super().place(*args, **kwargs)

    def build(self):
        self.password_time = Label(
            self, font=("Arial", 24), text="Senha: 1002\nGuiche: 03"
        )
        self.password_time.place(x=0, y=70, width=300)

        self.voltar = Button(
            self, text="Voltar", fg=GREEN, bg=LIGHTGREEN, command=self.voltar
        )
        self.voltar.place(x=75, y=200, width=150, height=40)

    def update_password_time(self, data):
        self.password_time.configure(text=data["message"])

    def voltar(self):
        self.app.set_base_config(APP_SIZE)
        self.switch_screen("home")
