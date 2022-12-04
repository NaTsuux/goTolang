from antlr4.tree import Tree

from .gen import goTolangVisitor, goTolangParser
from .exception import duplicatedLabelError
from .goTolangEnv import goTolangEnv


class goTolangPreVisitor(goTolangVisitor):
    def __init__(self, tree, env: goTolangEnv):
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
