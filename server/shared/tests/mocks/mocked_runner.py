from server.shared.runner import Runner


class MockedRunner(Runner):
    def routine(self):
        return "app is running"
