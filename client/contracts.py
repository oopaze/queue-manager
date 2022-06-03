from typing import Callable, TypedDict


class HomeButtonContract(TypedDict):
    name: str
    text: str


class EventContract(TypedDict):
    action: Callable
    message: bytes
