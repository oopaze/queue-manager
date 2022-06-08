from threading import Thread

from server.implementations.tests.mocks.socket_mock import MockedServer
from server.managers.client_manager import ClientManager
from server.managers.queue_manager import QueueManager


def teste_chamar_o_run_vai_iniciar_o_servidor():
    server = MockedServer()
    server_thread = Thread(target=server.run)
    server_thread.start()

    assert server.running is True
    assert server._running == "on"

    server.stop()
    server_thread.join()


def teste_iniciar_o_servidor_e_chamar_o_stop_vai_parar_o_servidor():
    server = MockedServer()
    server_thread = Thread(target=server.run)
    server_thread.start()

    assert server.running is True
    assert server._running == "on"

    server.stop()
    server_thread.join()

    assert server.running is False
    assert server._running == "off"


def teste_server_vai_instanciar_queue_manager():
    server = MockedServer()
    assert isinstance(server.queue_manager, QueueManager)


def teste_server_vai_instanciar_queue_manager():
    server = MockedServer()
    assert isinstance(server.client_manager, ClientManager)


def teste_routine_vai_adicionar_uma_nova_conexao():
    server = MockedServer()
    server.routine()

    assert len(server.client_manager.clients) == 1

    server.client_manager.clients[0]["connection"].stop()
    server.client_manager.clients[0]["connection"].client.close()
    server.client_manager.clients[0]["thread"].join()
