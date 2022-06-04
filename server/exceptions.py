class EmptyQueueException(Exception):
    def __init__(self, msg="A lista está vazia", *args, **kwargs):
        super().__init__(msg, *args, **kwargs)
