from socket import SO_REUSEADDR
from ssl import SOL_SOCKET
from server.implementations.server import Server


def run():
    server = Server()
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server.run()
