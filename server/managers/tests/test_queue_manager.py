import pytest
from server.exceptions import EmptyQueueException
from server.implementations.queue import Queue
from server.managers.queue_manager import QueueManager

normal_queue_items = ["N1", "N2", "N3", "N4"]
preferential_queue_items = ["P1"]


def test_adicionar_uma_senha_normal_na_fila():
    queue_manager = QueueManager()

    queue_manager.add()

    assert queue_manager.normal_queue.qsize() == 1


def test_adicionar_uma_senha_preferencial_na_fila():
    queue_manager = QueueManager()

    queue_manager.add(is_preferential=True)

    assert queue_manager.preferential_queue.qsize() == 1


def test_pegar_proximo_item_da_fila():
    queue_manager = QueueManager()

    queue_manager.add()

    assert queue_manager.next() == "N1"


def test_pegar_o_proximo_item_preferencial_da_fila():
    queue_manager = QueueManager()
    queue_manager.normal_queue = Queue.from_array(normal_queue_items)
    queue_manager.preferential_queue = Queue.from_array(
        preferential_queue_items, "P"
    )

    queue_manager.next()
    queue_manager.next()
    preferential_ticket = queue_manager.next()

    assert preferential_ticket == "P1"


def teste_pegar_o_terceiro_item_normal_quando_nao_houver_preferencial():
    queue_manager = QueueManager()
    queue_manager.normal_queue = Queue.from_array(normal_queue_items)

    queue_manager.next()
    queue_manager.next()
    normal_ticket = queue_manager.next()

    assert normal_ticket == "N3"


def teste_pedir_o_proximo_item_da_lista_vazia_deve_retornar_empty_exception():
    queue_manager = QueueManager()

    with pytest.raises(EmptyQueueException):
        queue_manager.next()


def teste_quantidade_items_chamados_se_inicia_em_0():
    queue_manager = QueueManager()

    assert queue_manager.amount_tickets_called == 0


def teste_quantidade_items_chamados_incrementa_conforme_chamamos_o_proximo_item():
    queue_manager = QueueManager()
    queue_manager.add()

    assert queue_manager.amount_tickets_called == 0

    queue_manager.next()

    assert queue_manager.amount_tickets_called == 1
