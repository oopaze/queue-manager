from json import dumps, loads
from typing import Any, Dict, List, TypedDict


class MessageContract(TypedDict):
    action: str
    args: List[Any]
    kwargs: Dict[str, Any]


class MessageManager:
    def decode(self, bytes_message: bytes) -> MessageContract:
        message = loads(bytes_message.decode(encoding="utf8"))
        message["args"] = message.get("args", [])
        message["kwargs"] = message.get("kwargs", {})
        return message

    def encode(self, message: Any):
        return dumps({"message": message}).encode(encoding="utf8")
