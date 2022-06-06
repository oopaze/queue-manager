from server.shared.runner import Runner


class MockedRunner(Runner):
    def run(self):
        return "app is running"
