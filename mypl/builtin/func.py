from mypl.base.ctx_node import CtxNode
from mypl.base.var import GoTolangVar, GoTolangArrEle
from mypl.exception import GoTolangFuncTypeError
from .array import GoTolangArrayBase, GoTolangArray, GoTolangDeque
from .doge import doge_str


class GoTolangFunc:
    def __init__(self, func, init=False):
        self.func = func
        self.init = init

    def __call__(self, *args, **kwargs):
        ret = self.func(*args, **kwargs)
        if isinstance(ret, GoTolangArrayBase):
            return CtxNode(is_ptr=True, type="array", value=ret, ctx=None)
        elif isinstance(ret, int):
            return CtxNode(is_ptr=False, type="int", value=ret, ctx=None)
        elif isinstance(ret, float):
            return CtxNode(is_ptr=False, type="float", value=ret, ctx=None)
        elif isinstance(ret, GoTolangArrEle):
            return CtxNode(is_ptr=True, type="ele ele", value=ret, ctx=None)
        elif isinstance(ret, str):
            return CtxNode(is_ptr=False, type="str", value=ret, ctx=None)
        else:
            raise Exception("Function return _type not implement yet")

    @property
    def value(self):
        return self


def _goTolang_print(*args):
    for arg in args:
        if isinstance(arg, GoTolangVar):
            print(arg.value, end='')
        else:
            print(arg, end='')
    return 0


def _goTolang_array_init(*args):
    i_args = tuple(int(arg) for arg in args)
    if len(args) == 1:
        return GoTolangDeque(i_args)
    else:
        return GoTolangArray(i_args)


def _goTolang_array_shape(*args):
    if len(args) != 2:
        raise Exception()  # TODO
    ele = args[0]
    if isinstance(ele, GoTolangVar):
        ele = ele.value
    if not isinstance(ele, GoTolangArrayBase):
        raise Exception()
    return ele.shape(int(args[1]))


def _goTolang_numin(*args):
    inp = float(input())
    for ele in args:
        if isinstance(ele, GoTolangVar):
            ele.value = ("float", inp)

        if not isinstance(ele, GoTolangArrEle) and not isinstance(ele, GoTolangVar):
            raise Exception()
        ele.value = ("float", inp)
    return 0


def _goTolang_array_strin(arr, *args, string=None):
    if not string:
        string = str(input())
    string = [c for c in string]
    ele: GoTolangArrEle = arr if len(args) == 0 else arr.get_ele(args)
    ele.pa.assign_str(string, ele)
    return 0


def _goTolang_deque_getb(arr):
    if isinstance(arr, GoTolangVar):
        arr = arr.value
    if not isinstance(arr, GoTolangDeque):
        raise GoTolangFuncTypeError("Can't apply method GETB on _type of {}.".format(arr.__class__.__name__))
    return arr.get_b()


def _goTolang_deque_popb(arr):
    if isinstance(arr, GoTolangVar):
        arr = arr.value
    if not isinstance(arr, GoTolangDeque):
        raise GoTolangFuncTypeError("Can't apply method GETB on _type of {}.".format(arr.__class__.__name__))
    arr.pop_b()
    return 0


def _goTolang_deque_pushb(arr, value):
    if isinstance(arr, GoTolangVar):
        arr = arr.value
    if not isinstance(arr, GoTolangDeque):
        raise GoTolangFuncTypeError("Can't apply method GETB on _type of {}.".format(arr.__class__.__name__))
    if isinstance(value, GoTolangVar):
        value = value.value
    arr.push_b(value)
    return 0


def _goTolang_deque_getf(arr):
    if isinstance(arr, GoTolangVar):
        arr = arr.value
    if not isinstance(arr, GoTolangDeque):
        raise GoTolangFuncTypeError("Can't apply method GETF on _type of {}.".format(arr.__class__.__name__))
    return arr.get_b()


def _goTolang_deque_popf(arr):
    if isinstance(arr, GoTolangVar):
        arr = arr.value
    if not isinstance(arr, GoTolangDeque):
        raise GoTolangFuncTypeError("Can't apply method GETF on _type of {}.".format(arr.__class__.__name__))
    arr.pop_b()
    return 0


def _goTolang_deque_pushf(arr, value):
    if isinstance(arr, GoTolangVar):
        arr = arr.value
    if not isinstance(arr, GoTolangDeque):
        raise GoTolangFuncTypeError("Can't apply method GETF on _type of {}.".format(arr.__class__.__name__))
    if isinstance(value, GoTolangVar):
        value = value.value
    arr.push_b(value)
    return 0


def _goTolang_doge(*args, **kwargs):
    print("Doge found! Say hello to him:\n{}".format(doge_str))
    return 0


goTolang_print = GoTolangFunc(_goTolang_print)
goTolang_numin = GoTolangFunc(_goTolang_numin, True)
goTolang_array_init = GoTolangFunc(_goTolang_array_init)
goTolang_array_shape = GoTolangFunc(_goTolang_array_shape)
goTolang_array_strin = GoTolangFunc(_goTolang_array_strin)
goTolang_array_getb = GoTolangFunc(_goTolang_deque_getb)
goTolang_array_popb = GoTolangFunc(_goTolang_deque_popb)
goTolang_array_pushb = GoTolangFunc(_goTolang_deque_pushb)
goTolang_array_getf = GoTolangFunc(_goTolang_deque_getf)
goTolang_array_popf = GoTolangFunc(_goTolang_deque_popf)
goTolang_array_pushf = GoTolangFunc(_goTolang_deque_pushf)
goTolang_doge = GoTolangFunc(_goTolang_doge)
