import socket
from time import sleep
from json import loads


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client.connect((socket.gethostbyname(socket.gethostname()), 50000))

TRANSFORM_TV_TEMPLATE = """{
    "action": "transform_tv_connection"
}"""

client.send(TRANSFORM_TV_TEMPLATE.encode("utf8"))

while True:
    received = client.recv(2048)

    if received:
        message = loads(received).get("message", None)

        if message:
            print(message)
