from threading import Thread

from server.implementations.tests.mocks.socket_mock import MockedServer


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
