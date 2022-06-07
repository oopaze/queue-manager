from json import dumps
from threading import Thread

from server.implementations.server import Server
from server.implementations.queue import Queue
from server.implementations.tests.mocks.mocked_client import MockedClient
from server.implementations.tsta_connection import TSTAConnection
from server.managers.message_manager import MessageManager

server = Server()
client = MockedClient()


def teste_se_conseguimos_instanciar_tsta_connection():
    connection = TSTAConnection(server=server, client=client)
    assert isinstance(connection, TSTAConnection)


def teste_message_manager_inicia_instaciado():
    connection = TSTAConnection(server=server, client=client)
    assert isinstance(connection.message_manager, MessageManager)


def teste_passar_uma_acao_invalida_vai_executar_invalid_action():
    client.set_message('{"action": "no"}')

    connection = TSTAConnection(server=server, client=client)
    conn_thread = Thread(target=connection.run)
    conn_thread.start()
    connection.stop()
    conn_thread.join()

    expected_send_message = dumps({"message": "Ação inválida"}).encode(
        encoding="utf8"
    )
    assert client.send_message == expected_send_message


def teste_passar_create_ticket_action_deve_gerar_um_ticket():
    server = Server()
    client = MockedClient()
    client.set_message('{"action": "create_ticket"}')

    connection = TSTAConnection(server=server, client=client)
    conn_thread = Thread(target=connection.run)
    conn_thread.start()
    connection.stop()
    conn_thread.join()

    expected_send_message = dumps({"message": "N1"}).encode(encoding="utf8")
    assert client.send_message == expected_send_message


def teste_passar_create_ticket_action_deve_gerar_um_ticket_preferencial():
    client.set_message('{"action": "create_ticket", "args": [true]}')

    connection = TSTAConnection(server=server, client=client)
    conn_thread = Thread(target=connection.run)
    conn_thread.start()
    connection.stop()
    conn_thread.join()

    expected_send_message = dumps({"message": "P1"}).encode(encoding="utf8")
    assert client.send_message == expected_send_message


def teste_passar_next_ticket_action_retorna_proximo_ticket():
    server = Server()
    server.queue_manager.normal_queue = Queue.from_array(["N1"], prefix="N")
    client.set_message('{"action": "next_ticket"}')

    connection = TSTAConnection(server=server, client=client)
    conn_thread = Thread(target=connection.run)
    conn_thread.start()
    connection.stop()
    conn_thread.join()

    expected_send_message = dumps({"message": "N1"}).encode(encoding="utf8")
    assert client.send_message == expected_send_message


def teste_passar_next_ticket_action_retorna_proximo_ticket_preferencial():
    server = Server()
    server.queue_manager.preferential_queue = Queue.from_array(["P1"], prefix="P")
    client.set_message('{"action": "next_ticket"}')

    connection = TSTAConnection(server=server, client=client)
    conn_thread = Thread(target=connection.run)
    conn_thread.start()
    connection.stop()
    conn_thread.join()

    expected_send_message = dumps({"message": "P1"}).encode(encoding="utf8")
    assert client.send_message == expected_send_message


def teste_pegar_o_proximo_ticket_quando_a_fila_estiver_vazia():
    server = Server()
    client.set_message('{"action": "next_ticket"}')

    connection = TSTAConnection(server=server, client=client)
    conn_thread = Thread(target=connection.run)
    conn_thread.start()
    connection.stop()
    conn_thread.join()

    expected_send_message = dumps({"message": "A lista está vazia"}).encode(
        encoding="utf8"
    )
    assert client.send_message == expected_send_message
