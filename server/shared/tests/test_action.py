import pytest

from server.shared.action import (
    Action,
    CreateTicketAction,
    NextTicketAction,
    TransformIntoTVAction,
)
from server.implementations.server import Server
from server.implementations.tsta_connection import TSTAConnection
from server.implementations.tv_connection import TVConnection

from server.implementations.tests.mocks.mocked_client import MockedClient
from server.shared.tests.mocks.mocked_action import MockedAction
from server.shared.tests.mocks.mocked_thread import FakeThread


def teste_tranformar_conexao_em_tv_connection(mocker):
    mocker.patch("server.shared.action.Thread", return_value=FakeThread)

    server = Server()
    client = MockedClient()
    connection = TSTAConnection(server, client)

    transform_tv_action = TransformIntoTVAction(server, connection)
    transform_tv_action.run()

    clients = server.client_manager.get_clients()
    transformed_connection = clients[0]["connection"]

    assert isinstance(transformed_connection, TVConnection)

    server.client_manager.stop_all_clients()


def teste_next_item_action_funciona():
    server = Server()
    server.queue_manager.add()

    next_ticket_action = NextTicketAction(server)

    next_ticket = next_ticket_action.run()

    assert next_ticket == "N1"


def teste_next_item_action_vai_retornar_mensagem_de_erro_quando_fila_tiver_vazia():
    server = Server()

    next_ticket_action = NextTicketAction(server)

    next_ticket = next_ticket_action.run()

    assert next_ticket == "A lista está vazia"


def teste_create_ticket_action_cria_um_novo_ticket_normal():
    server = Server()
    create_ticket_action = CreateTicketAction(server)
    create_ticket_action.run()

    created_item = server.queue_manager.next()

    assert created_item == "N1"


def teste_create_ticket_action_cria_um_novo_ticket_preferencial():
    server = Server()
    create_ticket_action = CreateTicketAction(server)
    create_ticket_action.run(is_preferential=True)

    created_item = server.queue_manager.next()

    assert created_item == "P1"


def test_classe_action_dar_erro_quando_tentamos_instanciar():
    with pytest.raises(TypeError):
        Action("teste", Server())


def testa_se_passar_um_master_diferente_de_server_dar_erro():
    with pytest.raises(TypeError):
        MockedAction("", "")


def testa_se_passar_name_vai_setar_atributo_name():
    action = MockedAction("teste", Server())

    assert action.name == "teste"


def teste_se_callback_eh_chamado_quando_passado():
    foo = 0

    def callback(*args, **kwargs):
        nonlocal foo
        foo += 1

    action_instance = MockedAction("teste", Server(), callback)
    action_instance.run()

    assert foo == 1
