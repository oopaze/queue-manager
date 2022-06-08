from multiprocessing import connection
from queue import Empty
from time import time
import pytest
from server.implementations.server import Server
from server.implementations.tests.mocks.mocked_client import MockedClient
from server.implementations.tv_connection import TVConnection

client = MockedClient()


def teste_tv_connection_instancia():
    server = Server()
    connection = TVConnection(server, client)

    assert isinstance(connection, TVConnection)


def teste_se_tv_connection_inicia_com_a_lista_de_eventos_vazia():
    server = Server()
    connection = TVConnection(server, client)
    assert connection.messages.empty() is True


def teste_adicionar_uma_nova_mensagem():
    server = Server()
    connection = TVConnection(server, client)
    connection.add_new_message("message")

    assert connection.messages.qsize() == 1


def teste_routine_vai_enviar_mensagem():
    server = Server()
    connection = TVConnection(server, client)
    connection.add_new_message("message")

    connection.routine()

    assert client.send_message == b'{"message": "message"}'


def teste_routine_espera_o_timeout_passado_antes_de_estourar_excecao_empty():
    server = Server()
    connection = TVConnection(server, client)
    timeout = 1

    start = time()
    connection.routine(timeout)
    end = time()

    timeout_expected_time = round(end - start)

    assert timeout == timeout_expected_time
