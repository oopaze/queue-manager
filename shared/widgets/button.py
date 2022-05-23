from tkinter import Button


class Button(Button):
    def place(self, *args, width: int = 200, height: int = 45, **kwargs):
        return super().place(*args, width=width, height=height, **kwargs)
