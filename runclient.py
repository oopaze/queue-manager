import socket
from time import sleep

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client.connect((socket.gethostbyname(socket.gethostname()), 50000))

while True:
    sleep(2)
    client.send("foo".encode())
