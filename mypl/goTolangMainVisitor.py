from typing import List

from antlr4.tree import Tree

from .gen import goTolangVisitor, goTolangParser
from .ctxNode import CtxNode
from .exception import GotoException, goTolangSymbolNotFoundError
from .goTolangEnv import goTolangEnv


class goTolangMainVisitor(goTolangVisitor):
    def __init__(self, tree, env: goTolangEnv):
        super().__init__()
        self.root = tree
        self.env = env
        self.resume_path = []

    def run(self, from_label: int):
        self.resume_path = self.env.get_label_path(from_label)
        node = self.resume_path.pop() if self.resume_path else None
        self.visitChildren(self.root, node)

    def get_ctx_node_value(self, ctx_node: CtxNode, ctx):
        if ctx_node.is_ptr:
            return self.env.get_symbol_value(ctx_node.value, ctx)
        else:
            return ctx_node.value

    def visitTerm(self, ctx: goTolangParser.TermContext):
        child_len = len(ctx.children)
        if child_len == 1:
            return ctx.children[0].accept(self)

        if ctx.STAR(0):
            # TODO type check
            left: CtxNode = ctx.children[0].accept(self)
            left_v = self.get_ctx_node_value(left, ctx)
            right: CtxNode = ctx.children[2].accept(self)
            right_v = self.get_ctx_node_value(right, ctx)
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

            # TODO QAQ so many todo
            if result.type == "int":
                if ctx.children[i].symbol.type == goTolangParser.ADD:
                    result_v = (self.get_ctx_node_value(result, ctx)
                                + self.get_ctx_node_value(right, ctx))
                    result = CtxNode(is_ptr=False, type="int", value=result_v)
                elif ctx.children[i].symbol.type == goTolangParser.MINUS:
                    result_v = (self.get_ctx_node_value(result, ctx)
                                - self.get_ctx_node_value(right, ctx))
                    result = CtxNode(is_ptr=False, type="int", value=result_v)
        return result

    def visitExpr_stmt(self, ctx: goTolangParser.Expr_stmtContext):
        if ctx.ASSIGN(0):
            left: CtxNode = ctx.children[0].accept(self)
            if not left.is_ptr:
                raise Exception("")  # TODO
            right: CtxNode = ctx.children[2].accept(self)
            # TODO todo
            right_v = self.get_ctx_node_value(right, ctx)

            # TODO 判断类型？
            self.env.set_symbol_value(left.value, right_v, ctx)

            return CtxNode(is_ptr=True, type=left.type, value=left.value)

        return ctx.testlist_star_expr(0).accept(self)

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

    def visitAtom_expr(self, ctx: goTolangParser.Atom_exprContext):
        atom: goTolangParser.AtomContext = ctx.atom()
        atom_ctx_node: CtxNode = atom.accept(self)
        atom_ctx_v = self.get_ctx_node_value(atom_ctx_node, ctx)
        trailer_ctx_nodes: List[CtxNode] = [tailer.accept(self) for tailer in ctx.trailer()]
        if len(trailer_ctx_nodes) == 0:
            return atom_ctx_node
        for trailer_ctx_node in trailer_ctx_nodes:
            if trailer_ctx_node.type == "arg list":
                # TODO func param check
                args = trailer_ctx_node.value
                atom_ctx_v(args[0].value)

    def visitArglist(self, ctx: goTolangParser.ArglistContext):
        # TODO support multi argument
        argument_ctx: CtxNode = ctx.argument(0).accept(self)
        arg_list = []
        if argument_ctx.is_ptr:
            arg_list.append(CtxNode(False, **self.env.get_symbol_meta(argument_ctx.value, ctx)))
        else:
            arg_list.append(CtxNode(False, argument_ctx.type, argument_ctx.value))
        return CtxNode(is_ptr=False, type="arg list", value=arg_list)

    def visitAtom(self, ctx: goTolangParser.AtomContext):
        if ctx.OPEN_PAREN() is not None:
            return ctx.testlist_comp().accept(self)
        if ctx.NAME():
            child = ctx.NAME()
            symbol = child.getText()
            if not self.env.get_symbol_exist(symbol, ctx):
                self.env.set_symbol_init(symbol, ctx)
            symbol_meta = self.env.get_symbol_meta(symbol, ctx)
            ctx_node = CtxNode(is_ptr=True, type=symbol_meta["type"], value=symbol)
        elif ctx.NUMBER():
            child = ctx.NUMBER()
            ctx_node = CtxNode(is_ptr=False, type="int", value=int(child.getText()))
        else:
            ctx_node = CtxNode(is_ptr=True, type=None, value=None)

        return ctx_node

    def visitComparison(self, ctx: goTolangParser.ComparisonContext):
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        # TODO long compare
        left: CtxNode = ctx.children[0].accept(self)
        left_v = self.get_ctx_node_value(left, ctx)
        right: CtxNode = ctx.children[2].accept(self)
        right_v = self.get_ctx_node_value(right, ctx)
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
