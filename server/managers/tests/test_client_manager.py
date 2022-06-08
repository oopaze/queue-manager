from threading import Thread

import pytest
from server.implementations.server import Server
from server.implementations.tsta_connection import TSTAConnection
from server.implementations.tv_connection import TVConnection
from server.managers.client_manager import ClientManager
from server.implementations.tests.mocks.mocked_client import MockedClient


def get_mocks():
    server = Server()
    client = MockedClient()
    connection = TVConnection(server, client)
    tsta_connection = TSTAConnection(server, client)
    thread = Thread(target=lambda: ...)

    return server, client, connection, tsta_connection, thread


def teste_se_cliente_manager_instancia():
    client_manager = ClientManager()

    assert isinstance(client_manager, ClientManager)


def teste_se_client_manager_tem_uma_lista_de_clients_vazia():
    client_manager = ClientManager()

    assert client_manager.clients == []


def teste_adicionar_novo_client_funciona():
    _, _, connection, _, thread = get_mocks()
    client_manager = ClientManager()

    client_manager.add_client(connection=connection, thread=thread)

    assert len(client_manager.clients) == 1


def teste_close_dead_clients_fecha_thread_mortas():
    client_manager = ClientManager()
    client_thread = Thread(target=lambda: ...)
    client_thread.start()

    client_manager.clients.append({"connection": "", "thread": client_thread})
    client_manager.clean_dead_clients()

    assert len(client_manager.clients) == 0


def teste_get_clients_retorna_lista_de_clientes():
    client_manager = ClientManager()

    clients = client_manager.get_clients()

    assert clients == client_manager.clients


@pytest.mark.parametrize("connection_type", (TVConnection, TSTAConnection))
def teste_get_clients_retorna_uma_lista_do_tipo_pedido(connection_type):
    _, _, connection, tsta_connection, thread = get_mocks()
    client_manager = ClientManager()
    client_manager.add_client(tsta_connection, thread)
    client_manager.add_client(connection, thread)

    clients = client_manager.get_clients(type=connection_type)

    for client in clients:
        assert isinstance(client["connection"], connection_type)


def teste_stop_all_clients_fecha_todos_os_clientes():
    _, _, connection, tsta_connection, thread = get_mocks()
    client_manager = ClientManager()
    client_manager.add_client(tsta_connection, thread)
    client_manager.add_client(connection, thread)

    client_manager.stop_all_clients()

    assert len(client_manager.clients) == 0
