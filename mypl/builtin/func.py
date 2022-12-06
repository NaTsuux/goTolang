from .array import GoTolangArray
from mypl.base.ctx_node import CtxNode
from mypl.base.var import GoTolangVar, GoTolangArrEle


class GoTolangFunc:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        ret = self.func(*args, **kwargs)
        if isinstance(ret, GoTolangArray):
            return CtxNode(is_ptr=True, type="array", value=ret, ctx=None)
        elif isinstance(ret, int):
            return CtxNode(is_ptr=False, type="int", value=ret, ctx=None)
        elif isinstance(ret, GoTolangArrEle):
            return CtxNode(is_ptr=True, type="arr ele", value=ret, ctx=None)
        else:
            raise Exception("Not implement")

    @property
    def value(self):
        return self


def _goTolang_print(*args):
    for arg in args:
        # TODO type check
        # print(arg)  # for debug
        if isinstance(arg, GoTolangVar):
            print(arg.value, end='')
        else:
            print(arg, end='')
    return 0


def _goTolang_array_init(*args):
    return GoTolangArray(args)


def _goTolang_array_shape(*args):
    if len(args) != 2:
        raise Exception()  # TODO
    ele = args[0]
    if isinstance(ele, GoTolangVar):
        ele = ele.value
    if not isinstance(ele, GoTolangArray):
        raise Exception()
    return ele.shape(args[1])


def _goTolang_array_numin(*args):
    inp = int(input())
    if len(args) == 1:
        args[0].value = ("int", inp)
    else:
        args[0].get_ele(args[1:]).value = ("int", inp)
    return 0


def _goTolang_array_strin(*args):
    inp = [c for c in str(input())]
    if len(args) == 1:
        ele: GoTolangArrEle = args[0]
    else:
        ele: GoTolangArrEle = args[0].get_ele(args[1:])
    ele.pa.assign_str(inp, ele)
    return 0


goTolang_print = GoTolangFunc(_goTolang_print)
goTolang_array_init = GoTolangFunc(_goTolang_array_init)
goTolang_array_shape = GoTolangFunc(_goTolang_array_shape)
goTolang_array_numin = GoTolangFunc(_goTolang_array_numin)
goTolang_array_strin = GoTolangFunc(_goTolang_array_strin)
