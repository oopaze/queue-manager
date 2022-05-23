from shared.app import App

from .defaults import APP_SIZE
from .screens.Stop import Stop
from .screens.Start import Start


def run_server():
    screens = [Start, Stop]

    app = App()

    app.set_base_config(APP_SIZE)
    app.set_screens(screens, "start")

    app.run()
