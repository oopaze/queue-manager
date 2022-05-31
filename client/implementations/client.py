from typing import Any, Dict
from json import dumps, loads

from client.managers.event_manager import EventManager
from shared.socket import Socket


class Client(Socket):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.event_manager = EventManager()

    def decode_message(self, message: bytes) -> Dict[str, Any]:
        return loads(message)

    def encode_message(self, message: Dict[str, Any]) -> bytes:
        return dumps(message, ensure_ascii=True, skipkeys=True).encode("utf-8")

    def run(self):
        self.start()
        address = (self.host, self.port)

        while self.running:
            event = self.event_manager.next()

            if event is not None:
                self.sendto(event["message"], address)
                received_encoded_message, _ = self.recvfrom(2048)
                received_decoded_message = self.decode_message(
                    received_encoded_message
                )
                self.event_manager.execute(received_decoded_message, event)

        self.close()
