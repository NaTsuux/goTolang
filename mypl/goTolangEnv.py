from .exception import goTolangSymbolNotFoundError


class goTolangEnv:
    def __init__(self):
        self.symbol_d = {
            "__global": {
                "PRINT": {"type": "built-in func", "value": print}
            }
        }
        self.label_d = {}

    def get_symbol_meta(self, symbol, ctx):
        # TODO use ctx
        res = self.symbol_d["__global"].get(symbol)
        if res is None:
            raise goTolangSymbolNotFoundError(symbol, ctx)
        return res

    def get_symbol_value(self, symbol, ctx):
        # TODO use ctx
        return self.symbol_d["__global"].get(symbol)["value"]

    def get_symbol_exist(self, symbol, ctx):
        # TODO use ctx
        return symbol in self.symbol_d["__global"]

    def set_symbol_value(self, symbol, value, ctx):
        if not self.get_symbol_exist(symbol, ctx):
            raise goTolangSymbolNotFoundError(symbol, ctx)
        # TODO use object to represent a variable
        self.symbol_d["__global"][symbol].update({"value": value})

    def set_symbol_init(self, symbol, ctx):
        # TODO use ctx and use object
        self.symbol_d["__global"][symbol] = {"type": "undefined", "value": None}

    def set_label_path(self, label, path):
        self.label_d[label] = path

    def get_label_path(self, label):
        if label is None:
            return None
        if label in self.label_d:
            return self.label_d.get(label).copy()
        return None

    def __str__(self):
        return "goTolang env object: (\n\tsymbol: {}\n\tlabel: {}\n)".format(
            self.symbol_d, self.label_d
        )
