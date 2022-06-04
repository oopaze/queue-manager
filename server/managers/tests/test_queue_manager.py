from server.exceptions import EmptyQueueException
from server.managers.queue_manager import QueueManager


def test_adicionar_uma_senha_normal_na_fila():
    queue_manager = QueueManager()

    queue_manager.add()

    assert len(queue_manager.normal_queue.tickets) == 1


def test_adicionar_uma_senha_preferencial_na_fila():
    queue_manager = QueueManager()

    queue_manager.add(is_preferential=True)

    assert len(queue_manager.preferential_queue.tickets) == 1


def test_pegar_proximo_item_da_fila():
    queue_manager = QueueManager()

    queue_manager.add()

    assert queue_manager.next() == "N1"


def test_pegar_proximo_item_preferencial_da_fila():
    queue_manager = QueueManager()
    queue_manager.normal_queue.tickets = ["N1", "N2", "N3", "N4"]
    queue_manager.preferential_queue.tickets = ["P1"]

    queue_manager.next()
    queue_manager.next()
    preferential_ticket = queue_manager.next()

    assert preferential_ticket == "P1"


def teste_pegar_o_terceiro_item_normal_quando_nao_houver_preferencial():
    queue_manager = QueueManager()
    queue_manager.normal_queue.tickets = ["N1", "N2", "N3", "N4"]

    queue_manager.next()
    queue_manager.next()
    normal_ticket = queue_manager.next()

    assert normal_ticket == "N3"


def teste_pedir_o_proximo_item_da_lista_vazia_deve_retornar_empty_exception():
    queue_manager = QueueManager()
    exception = None

    try:
        queue_manager.next()
    except Exception as exception_received:
        exception = exception_received

    assert type(exception) == EmptyQueueException
