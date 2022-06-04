from json import dumps, loads
from typing import Any, Dict


class MessageManager:
    def decode(self, bytes_message: bytes):
        return loads(bytes_message.decode(encoding="utf8"))

    def encode(self, message: Dict[str, Any]):
        return dumps(message).encode(encoding="utf8")
