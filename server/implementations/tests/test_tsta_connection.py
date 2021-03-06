from json import dumps

from server.implementations.server import Server
from server.implementations.queue import Queue
from server.implementations.tests.mocks.mocked_client import (
    MockedClient,
    MockedClientError,
)
from server.implementations.tsta_connection import TSTAConnection
from server.managers.message_manager import MessageManager

client = MockedClient()


def teste_se_conseguimos_instanciar_tsta_connection():
    server = Server()
    connection = TSTAConnection(server=server, client=client)
    assert isinstance(connection, TSTAConnection)


def teste_message_manager_inicia_instaciado():
    server = Server()
    connection = TSTAConnection(server=server, client=client)
    assert isinstance(connection.message_manager, MessageManager)


def teste_passar_uma_acao_invalida_vai_executar_invalid_action():
    server = Server()
    client.set_message('{"action": "no"}')

    connection = TSTAConnection(server=server, client=client)
    connection.routine()

    expected_send_message = dumps({"message": "Ação inválida"}).encode(
        encoding="utf8"
    )
    assert client.send_message == expected_send_message


def teste_passar_create_ticket_action_deve_gerar_um_ticket():
    server = Server()
    client.set_message('{"action": "create_ticket"}')

    connection = TSTAConnection(server=server, client=client)
    connection.routine()

    expected_send_message = dumps({"message": "N1"}).encode(encoding="utf8")
    assert client.send_message == expected_send_message


def teste_passar_create_ticket_action_com_args_deve_gerar_um_ticket_preferencial():
    server = Server()
    client.set_message('{"action": "create_ticket", "args": [true]}')

    connection = TSTAConnection(server=server, client=client)
    connection.routine()

    expected_send_message = dumps({"message": "P1"}).encode(encoding="utf8")
    assert client.send_message == expected_send_message


def teste_passar_create_ticket_action_com_kwargs_deve_gerar_um_ticket_preferencial():
    server = Server()
    client.set_message(
        '{"action": "create_ticket", "kwargs": {"is_preferential": true} }'
    )

    connection = TSTAConnection(server=server, client=client)
    connection.routine()

    expected_send_message = dumps({"message": "P1"}).encode(encoding="utf8")
    assert client.send_message == expected_send_message


def teste_passar_next_ticket_action_retorna_proximo_ticket():
    server = Server()
    server.queue_manager.normal_queue = Queue.from_array(["N1"], prefix="N")
    client.set_message('{"action": "next_ticket"}')

    connection = TSTAConnection(server=server, client=client)
    connection.routine()

    expected_send_message = dumps({"message": "N1"}).encode(encoding="utf8")
    assert client.send_message == expected_send_message


def teste_passar_next_ticket_action_retorna_proximo_ticket_preferencial():
    server = Server()
    server.queue_manager.preferential_queue = Queue.from_array(["P1"], prefix="P")
    client.set_message('{"action": "next_ticket"}')

    connection = TSTAConnection(server=server, client=client)
    connection.routine()

    expected_send_message = dumps({"message": "P1"}).encode(encoding="utf8")
    assert client.send_message == expected_send_message


def teste_pegar_o_proximo_ticket_quando_a_fila_estiver_vazia():
    server = Server()
    client.set_message('{"action": "next_ticket"}')

    connection = TSTAConnection(server=server, client=client)
    connection.routine()

    expected_send_message = dumps({"message": "A lista está vazia"}).encode(
        encoding="utf8"
    )
    assert client.send_message == expected_send_message


def teste_passar_uma_mensagem_nao_serializavel_vai_dar_acao_invalid():
    client.set_message("foo")

    server = Server()
    connection = TSTAConnection(server=server, client=client)
    connection.routine()

    expected_send_message = dumps({"message": "Ação inválida"}).encode(
        encoding="utf8"
    )
    assert client.send_message == expected_send_message


def teste_connection_para_se_client_desconectar():
    client = MockedClientError()

    server = Server()
    connection = TSTAConnection(server=server, client=client)
    connection.routine()

    assert connection.running is False


def teste_propagate_envia_mensagem_para_tvs():
    client.set_message('{"action": "next_ticket"}')

    server = Server()
    connection = TSTAConnection(server=server, client=client)
    connection.routine()

    expected_send_message = dumps({"message": "A lista está vazia"}).encode(
        encoding="utf8"
    )
    assert client.send_message == expected_send_message
