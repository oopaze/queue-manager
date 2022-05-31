from client.defaults import APP_SIZE
from client.implementations.app import ClientApp as App
from client.screens.home import Home
from client.screens.show_password import ShowPassword


def run_client():
    screens = [Home, ShowPassword]
    app = App()

    app.set_base_config(APP_SIZE)
    app.set_screens(screens)

    app.run()
