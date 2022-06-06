import pytest
from server.exceptions import EmptyQueueException
from server.implementations.queue import Queue


def teste_gerar_um_ticket_retorna_correto():
    queue = Queue(prefix="F")

    received_ticket = queue.generate()
    expected_ticket = "F0"

    assert received_ticket == expected_ticket


def teste_adicionar_um_ticket_retorna_correto():
    queue = Queue(prefix="F")

    received_ticket = queue.add()
    expected_ticket = "F1"

    assert received_ticket == expected_ticket


def teste_pedir_proximo_retorna_correto():
    queue = Queue(prefix="F")
    queue.put("F1")

    received_ticket = queue.next()
    expected_ticket = "F1"

    assert received_ticket == expected_ticket


def teste_pedir_proximo_com_fila_vazia_explode_error():
    queue = Queue(prefix="F")

    with pytest.raises(EmptyQueueException):
        queue.next()


def test_criar_uma_fila_apartir_de_um_array():
    array = ["P2", "P1", "P3"]

    queue = Queue.from_array(array)

    assert queue.qsize() == 3
    assert queue.get() == "P2"


def test_max_size_da_fila_eh_1000():
    queue = Queue(prefix="N")

    assert queue.maxsize == 1000
