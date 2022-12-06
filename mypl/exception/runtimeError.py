from .baseError import GoTolangBaseError


class goTolangRuntimeError(GoTolangBaseError):
    def __init__(self, ctx):
        super(goTolangRuntimeError, self).__init__(ctx)


class goTolangSymbolNotFoundError(goTolangRuntimeError):
    def __init__(self, symbol, ctx):
        super(goTolangSymbolNotFoundError, self).__init__(ctx)


class goTolangSymbolUndefinedError(goTolangRuntimeError):
    def __init__(self, symbol, ctx):
        super(goTolangSymbolUndefinedError, self).__init__(ctx)


class goTolangSymbolCannotCitedError(goTolangRuntimeError):
    def __init__(self, symbol, ctx):
        super(goTolangSymbolCannotCitedError, self).__init__(ctx)


class goTolangSymbolCannotAssignError(goTolangRuntimeError):
    def __init__(self, ctx_node, ctx):
        super(goTolangSymbolCannotAssignError, self).__init__(ctx)


class goTolangUnboundLocalError(goTolangRuntimeError):
    def __init__(self, symbol, ctx):
        super(goTolangUnboundLocalError, self).__init__(ctx)


class goTolangArrayDimNotOne(goTolangRuntimeError):
    def __init__(self, ctx):
        super(goTolangArrayDimNotOne, self).__init__(ctx)
