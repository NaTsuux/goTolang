from typing import Tuple
from mypl.base.var import GoTolangArrEle


class GoTolangArray:
    class ArrEleUndef:
        def __init__(self):
            pass
    undef = ArrEleUndef()

    def __init__(self, dim):
        try:
            self._ndim = len(dim)
            self._dim = dim
            self._list = [GoTolangArrEle("_", pa=self) if self._ndim == 1 else GoTolangArray(self._dim[1:])
                          for _ in range(self._dim[0])]
        except Exception:
            pass

    def shape(self, dim=-1):
        return self._dim if dim == -1 else self._dim[dim]

    def assign_str(self, string, begin):
        idx = self._list.index(begin)
        n = len(string)
        if self._dim[0] < idx + n:
            raise Exception()  # TODO out of index
        for i in range(n):
            self._list[idx + i].value = ("char", string[i])

    def get_ele(self, idx: Tuple):
        if len(idx) == 1:
            return self._list[idx[0]]
        return self._list[idx[0]].get_ele(idx[1:])

    @property
    def repr(self):  # for debug
        return self._list

    @property
    def value(self):
        return self
