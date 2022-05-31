from threading import Thread
from client.implementations.client import Client
from shared.app import App


class ClientApp(App):
    client: Client = None
    client_thread: Thread = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_client()

    def start_client(self):
        if self.client is None:
            self.client = Client(bind=False)
            self.client.app = self

        self.client_thread = Thread(target=self.client.run)
        self.client_thread.start()

    def stop_client(self):
        self.client.stop()
        self.client.close()
        self.client = None
