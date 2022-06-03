from tkinter import Tk
from typing import Dict, List, Tuple

from shared.widgets.screen import Screen


class App(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Gerenciador de Senhas - v1.0")
        self.resizable(0, 0)
        self.screens: Dict[str, Screen] = {}

    def set_base_config(self, app_size: Tuple[int]):
        self.geometry(
            "{0}x{1}+{2}+{3}".format(
                *app_size,
                self.winfo_rootx(),
                0,
            )
        )

    def set_screens(self, screens: List[Screen], initial_screen_name: str = "home"):
        for screen in screens:
            screen_instance = screen(self)
            self.screens[screen_instance.screen_name] = screen_instance

            if screen_instance.screen_name == initial_screen_name:
                screen_instance.place()

    def run(self):
        self.mainloop()
