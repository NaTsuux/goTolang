from antlr4.tree import Tree

from .gen import goTolangVisitor, goTolangParser
from .exception import duplicatedLabelError


class goTolangPreVisitor(goTolangVisitor):
    def __init__(self, tree):
        super().__init__()
        self.root = tree
        self.label_d = {}

        self.visitChildren(tree)

    def visitLabel_stmt(self, ctx: goTolangParser.Label_stmtContext):
        label = int(ctx.children[1].symbol.text)

        if self.label_d.get(label) is not None:
            raise duplicatedLabelError(label, ctx)

        path = []
        while ctx is not self.root:
            path.append(ctx)
            ctx = ctx.parentCtx
        self.label_d[label] = path
