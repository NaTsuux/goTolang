import functools

from antlr4 import ParserRuleContext


def change_env(func):
    @functools.wraps(func)
    def wrapper(self, ctx):
        if not isinstance(ctx, ParserRuleContext):
            raise Exception("FOR DEBUG Pre visitor")
        self.env.cur_symbol_env_to_ctx(ctx)
        ret = func(self, ctx)
        self.env.cur_symbol_env_to_parent()
        return ret

    return wrapper
