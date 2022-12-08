from abc import abstractmethod
from typing import Tuple

from mypl.base.var import GoTolangArrEle


class GoTolangArrayBase:

    def __init__(self, dim):
        self._ndim = len(dim)
        self._dim = dim
        self._list = []

    @abstractmethod
    def shape(self, dim):
        pass

    def get_ele(self, idx: Tuple):
        if len(idx) == 1:
            return self._list[idx[0]]
        return self._list[idx[0]].get_ele(idx[1:])

    def assign_str(self, string, begin):
        idx = self._list.index(begin)
        n = len(string)
        if self._dim[0] < idx + n:
            raise Exception()  # TODO out of index
        for i in range(n):
            self._list[idx + i].value = ("char", string[i])

    @property
    def value(self):
        return self


class GoTolangArray(GoTolangArrayBase):
    def __init__(self, dim):
        super(GoTolangArray, self).__init__(dim)
        self._list = [GoTolangArrEle("_", pa=self) if self._ndim == 1 else GoTolangArray(self._dim[1:])
                      for _ in range(self._dim[0])]

    def shape(self, dim=-1):
        return self._dim if dim == -1 else self._dim[dim]


class GoTolangDeque(GoTolangArrayBase):
    def __init__(self, dim):
        super(GoTolangDeque, self).__init__(dim)
        self._list = [GoTolangArrEle("_", pa=self) for _ in range(self._dim[0])]

    def shape(self, dim):
        return len(self._list)

    def get_b(self):
        return self._list[-1]

    def pop_b(self):
        self._list.pop()

    def push_b(self, value):
        self._list.append(value)

    def get_f(self):
        return self._list[0]

    def pop_f(self):
        self._list.pop(0)

    def push_f(self, value):
        self._list.insert(0, value)
