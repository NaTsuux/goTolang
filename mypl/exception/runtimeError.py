class goTolangRuntimeError(BaseException):
    def __init__(self):
        pass


class goTolangSymbolNotFoundError(goTolangRuntimeError):
    def __init__(self, symbol, ctx):
        super().__init__()
