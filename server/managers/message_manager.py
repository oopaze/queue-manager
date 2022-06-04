from json import dumps, loads
from typing import Any


class MessageManager:
    def decode(self, bytes_message: bytes):
        return loads(bytes_message.decode(encoding="utf8"))

    def encode(self, message: dict[str, Any]):
        return dumps(message).encode(encoding="utf8")
