import socket
from threading import Thread
from typing import List

from utils import create_client_connection

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('127.0.0.1', 50000))
server.listen(10)

thread_list: List[Thread] = []

while True:
    client, address = server.accept()

    connection = create_client_connection(client, address)
    
    client_thread = Thread(target=connection.run)
    client_thread.start()

    thread_list.append(client_thread)

    for idx, thread in thread_list:
        if not thread.is_alive():
            thread.join()
            thread_list.pop(idx)