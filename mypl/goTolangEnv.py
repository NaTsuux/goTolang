from .exception import goTolangSymbolNotFoundError
from .goTolangVar import goTolangVar
from .func import goTolang_print


class goTolangEnv:
    def __init__(self):
        self.symbol_d = {
            "__global": {
                "PRINT": goTolangVar("PRINT", "builtin func", goTolang_print)
            }
        }
        self.label_d = {}

    def get_symbol_meta(self, symbol, ctx) -> goTolangVar:
        # TODO use ctx
        res = self.symbol_d["__global"].get(symbol)
        if res is None:
            raise goTolangSymbolNotFoundError(symbol, ctx)
        return res

    # def get_ctx_node_value(self, symbol, ctx):
    #     """
    #     只有ctx_node.is_ptr 才需要转到这一层
    #     ctx在这一层用来确定 该变量名是在哪个作用域
    #     再往下就不需要ctx 变量本身不关心这个
    #     """
    #     return self.get_symbol_value(symbol, ctx)
    #
    # def get_symbol_value(self, symbol, ctx):
    #     # TODO use ctx
    #     return self.symbol_d["__global"].get(symbol).value

    def get_symbol_exist(self, symbol, ctx):
        # TODO use ctx
        return symbol in self.symbol_d["__global"]

    def set_symbol_value(self, symbol, type, value, ctx):
        if not self.get_symbol_exist(symbol, ctx):
            raise goTolangSymbolNotFoundError(symbol, ctx)
        # TODO use object to represent a variable
        self.symbol_d["__global"][symbol].value = (type, value)

    def set_symbol_init(self, symbol, ctx):
        # TODO use ctx and use object
        if not self.get_symbol_exist(symbol, ctx):
            self.symbol_d["__global"][symbol] = goTolangVar(symbol)

    def set_label_path(self, label, path):
        self.label_d[label] = path

    def get_label_path(self, label):
        if label is None:
            return None
        if label in self.label_d:
            return self.label_d.get(label).copy()
        return None

    def __str__(self):
        return "goTolangEnv object: (\n\tsymbol: {}\n\tlabel: {}\n)".format(
            self.symbol_d, self.label_d
        )
