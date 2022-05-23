from tkinter import Frame

from abc import abstractclassmethod


class Screen(Frame):
    _screen_name = "screen"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.build()

    @property
    def screen_name(self):
        return self._screen_name

    @abstractclassmethod
    def build(self, *args, **kwargs):
        raise NotImplementedError("Método não implementado")

    def place(self, *args, x: int = 0, y: int = 0, **kwargs):
        super().place(*args, x=x, y=y, **kwargs)

    def switch_screen(self, to: str, **kwargs):
        self.place_forget()
        screen = self.master.screens[to]
        screen.place(**kwargs)
