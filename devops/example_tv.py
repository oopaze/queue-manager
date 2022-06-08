from os import environ
import socket
from json import loads


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    client.connect((socket.gethostbyname(socket.gethostname()), 50000))
except:
    client.connect(("server", 50000))
    

TRANSFORM_TV_TEMPLATE = """{
    "action": "transform_tv_connection"
}"""

tv_id = environ.get("id", "")

client.send(TRANSFORM_TV_TEMPLATE.encode("utf8"))

while True:
    received = client.recv(2048)

    if received:
        message = loads(received).get("message", None)

        if message:
            print(f"(TV{tv_id}) - Próximo:", message)
