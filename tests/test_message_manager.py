from server.managers.message_manager import MessageManager

message_manager = MessageManager()


def teste_criar_instancia_do_message_manager():
    assert type(message_manager) == MessageManager


def teste_message_manager_pode_decodificar_uma_mensagem():
    bytes_message = '{"nome": "pedro"}'.encode("utf8")

    decoded_message = message_manager.decode(bytes_message)

    assert decoded_message == {"nome": "pedro"}


def teste_message_manager_pode_encodificar_uma_mensagem():
    decoded_message = {"nome": "pedro"}

    encoded_message = message_manager.encode(decoded_message)

    expected_encoded_message = '{"nome": "pedro"}'.encode("utf8")

    assert encoded_message == expected_encoded_message
