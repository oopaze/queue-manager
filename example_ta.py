import socket
from time import sleep
from json import loads


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client.connect((socket.gethostbyname(socket.gethostname()), 50000))

NEXT_TICKET_TEMPLATE = """{
    "action": "next_ticket"
}"""

while True:
    sleep(2)
    client.send(NEXT_TICKET_TEMPLATE.encode())
    print(loads(client.recv(2048)))
