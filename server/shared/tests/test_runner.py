from server.shared.tests.mocks.mocked_runner import MockedRunner


def teste_se_o_runner_inicia_offline():
    server = MockedRunner()

    assert server._running == "off"
    assert server.running is False


def teste_start_libera_runner_para_rodar():
    server = MockedRunner()
    server.start()

    assert server._running == "on"
    assert server.running is True


def teste_executar_start_e_depois_stop_liga_e_desliga_runner():
    server = MockedRunner()
    server.start()

    assert server._running == "on"
    assert server.running is True

    server.stop()

    assert server._running == "off"
    assert server.running is False
