from antlr4.tree import Tree

from .gen import goTolangVisitor, goTolangParser
from .exception import duplicatedLabelError, longComparisonError


class goTolangPreVisitor(goTolangVisitor):
    def __init__(self, tree, env):
        super().__init__()
        self.root = tree
        self.env = env

    def run(self):
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
