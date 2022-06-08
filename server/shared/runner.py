from abc import ABCMeta, abstractmethod


class Runner(metaclass=ABCMeta):
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

    def run(self):
        self.start()

        while self.running:
            self.routine()

    @abstractmethod
    def routine(self):
        ...
