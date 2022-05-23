import socket

mensagem_envio = """{
    "action": "add",
    "args": []
}"""


def run_client():
    porta = 5000
    host = socket.gethostbyname(socket.gethostname())

    cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        cliente.sendto(mensagem_envio.encode(), (host, porta))
        mensagem_serv, ip_serv = cliente.recvfrom(2048)
        if mensagem_serv:
            print(mensagem_serv.decode())
            break
        else:
            break
