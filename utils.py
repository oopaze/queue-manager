from abc import abstractclassmethod


class AbsctractConnection:
    ON = "on"
    OFF = "off"
    
    def __init__(self, client, address):
        self.client = client
        self.address = address
        self._running = self.OFF

    def start(self):
        self._running = self.ON

    def stop(self):
        self._running = self.OFF

    @property
    def running(self):
        return self._running == self.ON

    @abstractclassmethod
    def run(self):
        raise NotImplementedError("Método náo implementado")


class TVConnection(AbsctractConnection):
    def run(self):
        print("hehehe")


class TSTAConnection(AbsctractConnection):
    def run(self):
        print("suhasuhhasu")


def create_client_connection(client, address):
    message = client.recv(2048)

    if message.decode() == "TV":
        return TVConnection(client, address)
    else: 
        return TSTAConnection(client, address)
