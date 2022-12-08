from mypl import goTolangParser


class GoTolangBaseError(BaseException):
    def __init__(self, ctx):
        if ctx:
            while not isinstance(ctx, goTolangParser.Simple_stmtContext):
                ctx = ctx.parentCtx
        self.ctx = ctx

    def __repr__(self):
        if self.ctx is None:
            return "\n{} with no more information".format(self.__class__.__name__)
        else:
            return "\n{} at line {}: \n\t{}".format(
                self.__class__.__name__, self.ctx.start.line,
                self.ctx.start.source[1].strdata[self.ctx.start.start: self.ctx.stop.stop]
            )
