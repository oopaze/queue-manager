from tkinter import Button
from shared.app import App
from .defaults import APP_SIZE
from .screen.home import Home


def run_server():
    screens = [Home]

    app = App()

    app.set_base_config(APP_SIZE)
    app.set_screens(screens)

    app.run()
