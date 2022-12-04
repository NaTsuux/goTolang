from antlr4.tree import Tree

from .gen import goTolangVisitor, goTolangParser
from .ctxNode import CtxNode
from .exception import GotoException, goTolangSymbolNotFoundError


class goTolangMainVisitor(goTolangVisitor):
    def __init__(self, tree):
        super().__init__()
        self.root = tree
        self.symbol_d = {}
        self.label_d = {}
        self.resume_path = []

    def my_visit(self, path):
        self.resume_path = path.copy()
        node = self.resume_path.pop() if self.resume_path else None
        self.visitChildren(self.root, node)

    def get_value(self, symbol):
        symbol_meta = self.symbol_d.get(symbol)
        if symbol_meta is None:
            raise RuntimeError()  # TODO
        return symbol_meta["value"]

    def get_type(self, symbol):
        symbol_meta = self.symbol_d.get(symbol)
        if symbol_meta is None:
            raise Exception()  # TODO
        return symbol_meta["type"]

    def get_symbol_value(self, ctx: CtxNode):
        if ctx.is_ptr:
            return self.get_value(ctx.value)
        else:
            return ctx.value

    def exists(self, symbol):
        return self.symbol_d.get(symbol) is not None

    def visitTerm(self, ctx: goTolangParser.TermContext):
        child_len = len(ctx.children)
        if child_len == 1:
            return ctx.children[0].accept(self)

        if ctx.STAR(0):
            # TODO type check
            left: CtxNode = ctx.children[0].accept(self)
            left_v = self.get_symbol_value(left)
            right: CtxNode = ctx.children[2].accept(self)
            right_v = self.get_symbol_value(right)
            return CtxNode(is_ptr=False, type="int", value=left_v * right_v)

    def visitArith_expr(self, ctx: goTolangParser.Arith_exprContext):
        child_len = len(ctx.children)
        if child_len == 1:
            return ctx.children[0].accept(self)
        result: CtxNode = ctx.children[0].accept(self)

        for i in range(1, child_len, 2):
            # why None?
            right: CtxNode = ctx.children[i + 1].accept(self)
            if result.type != right.type:
                raise Exception("Can't calculate between different type {} and {}".format(result.type, right.type))

            if result.type == "int":
                if ctx.children[i].symbol.type == goTolangParser.ADD:
                    result_v = ((self.get_value(result.value) if result.is_ptr else result.value)
                                + (self.get_value(right.value) if right.is_ptr else right.value))
                    result = CtxNode(is_ptr=False, type="int", value=result_v)
                elif ctx.children[i].symbol.type == goTolangParser.MINUS:
                    result_v = ((self.get_value(result.value) if result.is_ptr else result.value)
                                - (self.get_value(right.value) if right.is_ptr else right.value))
                    result = CtxNode(is_ptr=False, type="int", value=result_v)
        return result

    def visitExpr_stmt(self, ctx: goTolangParser.Expr_stmtContext):

        if ctx.ASSIGN(0):
            left: CtxNode = ctx.children[0].accept(self)
            if not left.is_ptr:
                raise Exception("")  # TODO
            right: CtxNode = ctx.children[2].accept(self)
            right_v = self.get_type(right.value) if right.is_ptr else right.value

            # TODO 判断类型？

            self.symbol_d[left.value] = {"type": right.type, "value": right_v}

            return CtxNode(is_ptr=True, type=left.type, value=left.value)

    def visitBto(self, ctx: goTolangParser.BtoContext):
        label = int(ctx.NUMBER().getText())
        raise GotoException(label)

    def visitBif(self, ctx: goTolangParser.BifContext):
        label = int(ctx.NUMBER().getText())
        cond: CtxNode = ctx.or_test().accept(self)
        if cond.value:
            raise GotoException(label)
        else:
            return None

    def visitAtom(self, ctx: goTolangParser.AtomContext):
        if ctx.OPEN_PAREN() is not None:
            return ctx.testlist_comp().accept(self)
        child: Tree.TerminalNodeImpl = ctx.children[0]
        if child.symbol.type == goTolangParser.NAME:
            if not self.exists(child.symbol.text):
                self.symbol_d[child.symbol.text] = {"type": "int", "value": None}  # TODO
            ctx_node = CtxNode(is_ptr=True, type=self.get_type(child.symbol.text), value=child.symbol.text)
        elif child.symbol.type == goTolangParser.NUMBER:
            ctx_node = CtxNode(is_ptr=False, type="int", value=int(child.symbol.text))
        else:
            ctx_node = CtxNode(is_ptr=True, type=None)

        return ctx_node

    def visitComparison(self, ctx: goTolangParser.ComparisonContext):
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        # TODO long compare
        left: CtxNode = ctx.children[0].accept(self)
        left_v = self.get_symbol_value(left)
        right: CtxNode = ctx.children[2].accept(self)
        right_v = self.get_symbol_value(right)
        if ctx.comp_op(0).LESS_THAN():
            return CtxNode(is_ptr=False, type="bool", value=(left_v < right_v))
        # TODO other ops

    def visitChildren(self, node, begin_node=None):
        result = self.defaultResult()
        n = node.getChildCount()
        si = 0 if not begin_node else node.children.index(begin_node)

        for i in range(si, n):
            c = node.getChild(i)
            if not isinstance(c, Tree.TerminalNodeImpl):
                result = c.accept(self)

        return result

    # Visit a parse tree produced by goTolangParser#file_input.
    def visitFile_input(self, ctx: goTolangParser.File_inputContext):
        if self.resume_path:
            node = self.resume_path.pop()
            return self.visitChildren(ctx, node)
        else:
            return self.visitChildren(ctx)

    def visitFile_input_no_eof(self, ctx: goTolangParser.File_input_no_eofContext):
        if self.resume_path:
            node = self.resume_path.pop()
            return self.visitChildren(ctx, node)
        else:
            return self.visitChildren(ctx)

    def visitStmt(self, ctx: goTolangParser.StmtContext):
        if self.resume_path:
            node = self.resume_path.pop()
            return self.visitChildren(ctx, node)
        else:
            return self.visitChildren(ctx)

    def visitSimple_stmt(self, ctx: goTolangParser.Simple_stmtContext):
        if self.resume_path:
            node = self.resume_path.pop()
            return self.visitChildren(ctx, node)
        else:
            return self.visitChildren(ctx)

    def visitBlabel(self, ctx: goTolangParser.BlabelContext):
        if self.resume_path:
            node = self.resume_path.pop()
            return self.visitChildren(ctx, node)
        else:
            return self.visitChildren(ctx)
