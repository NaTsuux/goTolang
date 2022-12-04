class goTolangRuntimeError(BaseException):
    def __init__(self):
        pass


class goTolangSymbolNotFoundError(goTolangRuntimeError):
    def __init__(self):
        super().__init__()
