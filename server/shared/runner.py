from abc import abstractmethod


class Runner:
    ON = "on"
    OFF = "off"

    def __init__(self):
        self._running = self.OFF

    @property
    def running(self):
        return self._running == self.ON

    def stop(self):
        self._running = self.OFF

    def start(self):
        self._running = self.ON

    @abstractmethod
    def run():
        raise NotImplementedError("Método não implementado")
