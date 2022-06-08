from secrets import choice
import socket
from time import sleep
from json import loads


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    client.connect((socket.gethostbyname(socket.gethostname()), 50000))
except:
    client.connect(("server", 50000))


def generate_message():
    message = choice([PREFERENTIAL_TEMPLATE, NORMAL_TICKET_TEMPLATE])
    return message.encode("utf8")


PREFERENTIAL_TEMPLATE = """{
    "action": "create_ticket",
    "kwargs": {
        "is_preferential": true
    }
}"""

NORMAL_TICKET_TEMPLATE = """{
    "action": "create_ticket"
}"""

print("Iniciando criação de novas senhas")

while True:
    sleep(2)  # gerando uma senha por segundo
    client.send(generate_message())
    nova_senha = loads(client.recv(2048)).get("message")
    print("(Gerador de senha) - A nova senha é:", nova_senha)
