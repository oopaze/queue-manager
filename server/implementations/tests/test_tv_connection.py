from multiprocessing import connection
from queue import Empty
from time import time
import pytest
from server.implementations.server import Server
from server.implementations.tests.mocks.mocked_client import MockedClient
from server.implementations.tv_connection import TVConnection

server = Server()
client = MockedClient()


def teste_tv_connection_instancia():
    connection = TVConnection(server, client)

    assert isinstance(connection, TVConnection)


def teste_se_tv_connection_inicia_com_a_lista_de_eventos_vazia():
    connection = TVConnection(server, client)
    assert connection.events.empty() is True


def teste_add_um_novo_evento_funciona():
    connection = TVConnection(server, client)
    connection.add_new_event(lambda: print("olá"))

    assert connection.events.qsize() == 1


@pytest.mark.parametrize(
    "event", ["evento", ["evento"], {"evento": "event"}, 1, object()]
)
def teste_add_um_novo_evento_do_tipo_diferente_de_funcao_estoura_excecao(event):
    connection = TVConnection(server, client)

    with pytest.raises(TypeError):
        connection.add_new_event(event=event)


def teste_routine_roda_evento_adicionado():
    foo = 0

    def event():
        nonlocal foo
        foo += 1

    connection = TVConnection(server, client)
    connection.add_new_event(event)
    connection.routine()

    assert foo == 1


def teste_routine_espera_o_timeout_passado_antes_de_estourar_excecao_empty():
    connection = TVConnection(server, client)
    timeout = 1

    start = time()
    connection.routine(timeout)
    end = time()

    timeout_expected_time = round(end - start)

    assert timeout == timeout_expected_time
