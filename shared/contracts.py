from typing import Any, Dict, List, TypedDict


class MessageContract(TypedDict):
    action: str
    args: List[Any]
    kwargs: Dict[str, Any]

