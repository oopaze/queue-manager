from queue import Queue
from typing import Any, Dict, List

from client.contracts import EventContract


class EventManager:
    events: "Queue[EventContract]" = Queue()

    def default_action(self, *args):
        return

    def execute(self, data: Dict[str, Any], event: EventContract):
        action = event.get("action", self.default_action)
        return action(data)

    def add(self, event: EventContract):
        self.events.put(event)

    def next(self) -> EventContract:
        if not self.events.empty():
            return self.events.get()
        else:
            return None
