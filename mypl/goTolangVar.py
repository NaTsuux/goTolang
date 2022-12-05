from typing import Tuple, Any

from .exception import goTolangSymbolUndefinedError


class goTolangVar:

    def __init__(self, name, type="undefined", value=None, is_const=False):
        self.is_const = is_const
        self._name = name
        self.type = type
        self._value = value

    @property
    def value(self):

        if self.type == "undefined":
            raise goTolangSymbolUndefinedError(self.name, None)
        return self._value

    @value.setter
    def value(self, t_v: Tuple[str, Any]):
        type, value = t_v
        if self.type != type:
            pass
        self.type, self._value = type, value

    @property
    def name(self):
        return self._name