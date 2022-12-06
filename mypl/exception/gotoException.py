class GotoException(BaseException):
    def __init__(self, label):
        self.label = label


class GobackException(BaseException):
    def __init__(self, label):
        self.label = label
