from .baseError import GoTolangBaseError


class GoTolangRuntimeError(GoTolangBaseError):
    def __init__(self, ctx):
        super(GoTolangRuntimeError, self).__init__(ctx)


class GoTolangSymbolNotFoundError(GoTolangRuntimeError):
    def __init__(self, symbol, ctx):
        super(GoTolangSymbolNotFoundError, self).__init__(ctx)


class GoTolangSymbolUndefinedError(GoTolangRuntimeError):
    def __init__(self, symbol, ctx):
        super(GoTolangSymbolUndefinedError, self).__init__(ctx)


class GoTolangSymbolCannotCitedError(GoTolangRuntimeError):
    def __init__(self, symbol, ctx):
        super(GoTolangSymbolCannotCitedError, self).__init__(ctx)


class GoTolangSymbolCannotAssignError(GoTolangRuntimeError):
    def __init__(self, ctx_node, ctx):
        super(GoTolangSymbolCannotAssignError, self).__init__(ctx)


class GoTolangUnboundLocalError(GoTolangRuntimeError):
    def __init__(self, symbol, ctx):
        super(GoTolangUnboundLocalError, self).__init__(ctx)


class GoTolangFuncTypeError(GoTolangRuntimeError):
    def __init__(self, ctx):
        super(GoTolangFuncTypeError, self).__init__(ctx)


class GoTolangRedunGobackError(GoTolangRuntimeError):
    def __init__(self, ctx):
        super(GoTolangRedunGobackError, self).__init__(ctx)
