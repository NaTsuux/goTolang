from typing import List

from mypl.builtin import *
from mypl.exception import GoTolangSymbolNotFoundError, GoTolangRedunGobackError


class GoTolangEnv:
    def __init__(self):
        self.symbol_env = GoTolangSymbolEnv(self)
        self.symbol_env.symbol_d.update({
            "PRINT": goTolang_print,
            "ARRAY": goTolang_array_init,
            "SHAPE": goTolang_array_shape,
            "NUMIN": goTolang_numin,
            "STRIN": goTolang_array_strin,
            "GETB": goTolang_array_getb,
            "POPB": goTolang_array_popb,
            "PUSHB": goTolang_array_pushb,
        })
        self.label_env = {}
        self.goto_env = {}
        self.last_goto = {}  # label: [ctx, ...]
        self.cur_symbol_env = self.symbol_env

    def cur_symbol_env_clear(self):
        self.cur_symbol_env = self.symbol_env

    def cur_symbol_env_to_ctx(self, ctx):
        self.cur_symbol_env = self.cur_symbol_env.to_env(ctx)

    def cur_symbol_env_to_parent(self):
        self.cur_symbol_env = self.cur_symbol_env.parent

    def get_symbol_meta(self, *args, **kwargs):
        return self.cur_symbol_env.get_symbol_meta(*args, **kwargs)

    def get_symbol_exist(self, *args, **kwargs):
        return self.cur_symbol_env.get_symbol_exist(*args, **kwargs)

    def set_symbol_value(self, *args, **kwargs):
        return self.cur_symbol_env.set_symbol_value(*args, **kwargs)

    def set_symbol_init(self, *args, **kwargs):
        return self.cur_symbol_env.set_symbol_init(*args, **kwargs)

    def set_label_path(self, label, path):
        self.label_env[label] = path

    def set_goto_path(self, label, path):
        if not self.goto_env.get(label):
            self.goto_env[label] = []
        self.goto_env[label].append(path)

    def get_last_goto_path(self, label):
        ctx = self.last_goto.get(label)
        if not ctx:
            raise GoTolangRedunGobackError(None)
        ctx: List = ctx.pop(0)
        for path in self.goto_env[label]:
            if ctx == path[0]:
                return path.copy()
        raise Exception("No goto path found")

    def get_label_path(self, label):
        if label is None:
            return None
        if label in self.label_env:
            return self.label_env.get(label).copy()
        return None

    def __str__(self):
        return "goTolangEnv object: (\n\tsymbol: {}\n\tlabel: {}\n)".format(
            self.symbol_env, self.label_env
        )


class GoTolangSymbolEnv:
    def __init__(self, parent):
        self.parent = parent
        self.is_root = isinstance(parent, GoTolangEnv)
        self.symbol_d = {}

    def get_symbol_meta(self, symbol, ctx) -> GoTolangVar:
        res = self.symbol_d.get(symbol)
        if res is not None:
            return res
        if self.is_root:
            raise GoTolangSymbolNotFoundError(symbol, ctx)
        return self.parent.get_symbol_meta(symbol, ctx)

    def get_symbol_exist(self, symbol, ctx):
        res = symbol in self.symbol_d
        return res if self.is_root else (res or self.parent.get_symbol_exist(symbol, ctx))

    def set_symbol_value(self, symbol, type, value, ctx):
        self.get_symbol_meta(symbol, ctx).value = (type, value)
        return True

    def set_symbol_init(self, symbol, ctx):
        if symbol not in self.symbol_d:
            self.symbol_d[symbol] = GoTolangVar(symbol)

    def to_env(self, ctx):
        if not self.symbol_d.get(ctx):
            self.symbol_d[ctx] = GoTolangSymbolEnv(self)
        return self.symbol_d[ctx]
