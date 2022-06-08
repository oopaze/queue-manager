from server.shared.action import Action


class MockedAction(Action):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def action(self):
        ...
