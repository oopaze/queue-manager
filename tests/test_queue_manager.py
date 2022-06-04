from server.managers.queue_manager import QueueManager


def test_adicionar_uma_senha_normal_na_fila():
    queue_manager = QueueManager()

    queue_manager.add()

    assert len(queue_manager.normal_tickets) == 1


def test_adicionar_uma_senha_preferencial_na_fila():
    queue_manager = QueueManager()

    queue_manager.add(is_preferential=True)

    assert len(queue_manager.preferential_tickets) == 1


def test_pegar_proximo_item_da_fila():
    queue_manager = QueueManager()

    queue_manager.add()

    assert queue_manager.next() == 1001


def test_pegar_proximo_item_preferencial_da_fila():
    queue_manager = QueueManager()

    for _ in range(0, 4):
        queue_manager.add()

    queue_manager.add(is_preferential=True)

    queue_manager.next()
    queue_manager.next()
    preferential_ticket = queue_manager.next()

    assert preferential_ticket == 1005


def teste_pegar_o_terceiro_item_normal_quando_nao_houver_preferencial():
    queue_manager = QueueManager()

    for _ in range(0, 3):
        queue_manager.add()

    queue_manager.next()
    queue_manager.next()
    preferential_ticket = queue_manager.next()

    assert preferential_ticket == 1003
