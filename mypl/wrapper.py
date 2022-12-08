import functools

from antlr4 import ParserRuleContext

from mypl.gen import goTolangParser


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


def goto_resume(func):
    @functools.wraps(func)
    def wrapper(self, ctx):
        if self.resume_path:
            node = self.resume_path.pop()
            return self.visitChildren(ctx, node) if not isinstance(ctx, goTolangParser.BgotoContext) else None
        else:
            return self.visitChildren(ctx)

    return wrapper
