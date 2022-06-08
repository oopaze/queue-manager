class MockedClient:
    message = b""
    send_message = ""

    def set_message(self, new_message):
        self.message = new_message.encode()

    def recv(self, *args, **kwargs):
        return self.message

    def close(self):
        ...

    def send(self, message):
        self.send_message = message
        self.message = b""


class MockedClientError(MockedClient):
    def recv(self, *args, **kwargs):
        raise ConnectionResetError()
