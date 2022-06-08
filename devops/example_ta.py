import socket
from time import sleep
from json import loads


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    client.connect((socket.gethostbyname(socket.gethostname()), 50000))
except:
    client.connect(("server", 50000))

NEXT_TICKET_TEMPLATE = """{
    "action": "next_ticket"
}"""

print("Iniciando chamada ao próximo ticket")

while True:
    sleep(5)
    client.send(NEXT_TICKET_TEMPLATE.encode())
    proximo = loads(client.recv(2048)).get("message")
    print("(Atendente) - Próximo Ticket:", proximo)