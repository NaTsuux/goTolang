from mypl.exception import GoTolangSymbolCannotCitedError


class CtxNode:

    def __init__(self, is_ptr, type, value, ctx):
        self.is_ptr = is_ptr
        self.type = type
        self._value = value
        self.ctx = ctx

    @property
    def cite(self):
        if not self.is_ptr:
            raise GoTolangSymbolCannotCitedError(self._value, self.ctx)
        return self._value

    @property
    def value(self):
        if self.is_ptr:
            return self._value.value
        else:
            return self._value

    @value.setter
    def value(self, value):
        self._value = value
