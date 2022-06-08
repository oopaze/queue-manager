import pytest
from server.managers.queue_manager import QueueManager
from server.shared.tests.mocks.mocked_connection import MockedConnection


def teste_atributo_queue_manager_inicia_none():
    base_connection = MockedConnection()

    assert base_connection.queue_manager is None


def teste_queue_manager_pode_ser_setado_normalmente():
    queue_manager_instance = QueueManager()
    base_connection = MockedConnection()

    base_connection.queue_manager = queue_manager_instance

    assert base_connection.queue_manager == queue_manager_instance


def teste_setar_queue_manager_com_um_tipo_diferente_estoura_um_erro():
    base_connection = MockedConnection()

    with pytest.raises(TypeError):
        base_connection.queue_manager = 1
