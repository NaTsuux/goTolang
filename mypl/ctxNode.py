from .exception import goTolangSymbolCannotCitedError


class CtxNode:
    env = None

    def __init__(self, is_ptr, type, value, ctx):
        self.is_ptr = is_ptr
        self.type = type
        self._value = value
        self.ctx = ctx

    @property
    def cite(self):
        if not self.is_ptr:
            # TODO ctx
            raise goTolangSymbolCannotCitedError(self._value, None)
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
