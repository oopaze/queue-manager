from client.defaults import APP_SIZE
from client.implementations.app import ClientApp as App
from client.screens.home import Home


def run_client():
    screens = [Home]
    app = App()

    app.set_base_config(APP_SIZE)
    app.set_screens(screens)
    app.run()
