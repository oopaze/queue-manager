import socket
from time import sleep

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client.connect(('localhost', 50000))

client.send("watcher".encode())

while True:
    message = client.recv(2048)
    print(message.decode())
    sleep(2)