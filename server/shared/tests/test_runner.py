import pytest
from server.shared.runner import Runner
from server.shared.tests.mocks.mocked_runner import MockedRunner


def teste_se_o_runner_inicia_offline():
    runner = MockedRunner()

    assert runner._running == "off"
    assert runner.running is False


def teste_start_libera_runner_para_rodar():
    runner = MockedRunner()
    runner.start()

    assert runner._running == "on"
    assert runner.running is True


def teste_executar_start_e_depois_stop_liga_e_desliga_runner():
    runner = MockedRunner()
    runner.start()

    assert runner._running == "on"
    assert runner.running is True

    runner.stop()

    assert runner._running == "off"
    assert runner.running is False


def teste_instanciar_runner_sem_implementar_run_explode_um_error():
    exception_expected = None

    with pytest.raises(TypeError):
        runner = Runner()
