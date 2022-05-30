from threading import Thread
from client.implementations.client import Client
from shared.app import App


class ClientApp(App):
    client_thread = None
    client_instance = None

    @classmethod
    def start_client(cls):
        if cls.client_instance is None:
            cls.client_instance = Client()

        if cls.client_thread is None:
            cls.client_thread = Thread(cls.client_instance.run)

        cls.client_thread.start()

    @classmethod
    def stop_client(cls):
        if cls.client_instance.running:
            cls.client_instance.stop()

    def run(self):
        ClientApp.start_client()
        super().run()
        ClientApp.stop_client()
