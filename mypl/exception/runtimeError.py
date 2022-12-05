class goTolangRuntimeError(BaseException):
    def __init__(self):
        pass


class goTolangSymbolNotFoundError(goTolangRuntimeError):
    def __init__(self, symbol, ctx):
        super(goTolangSymbolNotFoundError, self).__init__()


class goTolangSymbolUndefinedError(goTolangRuntimeError):
    def __init__(self, symbol, ctx):
        super(goTolangSymbolUndefinedError, self).__init__()


class goTolangSymbolCannotCitedError(goTolangRuntimeError):
    def __init__(self, symbol, ctx):
        super(goTolangSymbolCannotCitedError, self).__init__()
