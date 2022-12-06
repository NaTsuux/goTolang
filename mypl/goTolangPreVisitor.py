from .exception import duplicatedLabelError, longComparisonError
from .gen import goTolangVisitor, goTolangParser
from .base.env import GoTolangEnv
from .wrapper import change_env


class goTolangPreVisitor(goTolangVisitor):
    def __init__(self, tree, env):
        super().__init__()
        self.root = tree
        self.env: GoTolangEnv = env

    def run(self):
        self.env.cur_symbol_env_clear()
        self.visitChildren(self.root)

    def visitLabel_stmt(self, ctx: goTolangParser.Label_stmtContext):
        label = int(ctx.NUMBER().getText())

        if self.env.get_label_path(label) is not None:
            raise duplicatedLabelError(label, ctx)

        path = []
        while ctx is not self.root:
            path.append(ctx)
            ctx = ctx.parentCtx
        self.env.set_label_path(label, path)

    def visitComparison(self, ctx: goTolangParser.ComparisonContext):
        if len(ctx.comp_op()) > 1:
            raise longComparisonError(ctx)
        return self.visitChildren(ctx)

    @change_env
    def visitFile_input_no_eof(self, ctx: goTolangParser.File_input_no_eofContext):
        return self.visitChildren(ctx)

    # def visitSuite(self, ctx: goTolangParser.SuiteContext):
    #     return self.visitChildren(ctx)
