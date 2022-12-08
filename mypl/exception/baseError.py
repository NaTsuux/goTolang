from mypl import goTolangParser


class GoTolangBaseError(BaseException):
    def __init__(self, ctx):
        self.ctx = ctx

    def __repr__(self):
        if self.ctx is None:
            return "\n{} with no more information".format(self.__class__.__name__)
        else:
            ctx = self.ctx
            while not isinstance(ctx, goTolangParser.Simple_stmtContext):
                ctx = ctx.parentCtx

            return "\n{} at line {}: \n\t{}\n\t{}".format(
                self.__class__.__name__, ctx.start.line,
                ctx.start.source[1].strdata[ctx.start.start: ctx.stop.stop + 1].strip(),
                " " * (self.ctx.start.start - ctx.start.start) + "^"
            )
