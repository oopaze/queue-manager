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
    queue.tickets = ["F1"]

    received_ticket = queue.next()
    expected_ticket = "F1"

    assert received_ticket == expected_ticket


def teste_pedir_proximo_com_fila_vazia_explode_error():
    queue = Queue(prefix="F")

    expected_exception = None

    try:
        queue.next()
    except Exception as exception:
        expected_exception = exception

    assert type(expected_exception) == EmptyQueueException
