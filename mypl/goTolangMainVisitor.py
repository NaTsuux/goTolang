from typing import List

from antlr4.tree import Tree

from .base import GoTolangEnv, CtxNode
from .builtin import GoTolangArrayBase, GoTolangFunc
from .exception import *
from .exception.gotoException import GobackException
from .gen import goTolangVisitor, goTolangParser
from .wrapper import change_env, goto_resume


class goTolangMainVisitor(goTolangVisitor):
    def __init__(self, tree, env: GoTolangEnv):
        super().__init__()
        self.root = tree
        self.env = env
        self.resume_path = []
        self.left = False

    def run(self, to_label: int = None, back_label: int = None):
        self.env.cur_symbol_env_clear()
        if not to_label and not back_label:
            return self.visitChildren(self.root)

        if to_label:
            self.resume_path = self.env.get_label_path(to_label)
        elif back_label:
            self.resume_path = self.env.get_last_goto_path(back_label)

        node = self.resume_path.pop()
        return self.visitChildren(self.root, node)

    def visitIf_stmt(self, ctx: goTolangParser.If_stmtContext):
        if self.resume_path:
            next_node = self.resume_path.pop()
            return next_node.accept(self)

        test_suite_list = list(zip(ctx.or_test(), ctx.suite()))
        for test_ctx, suite_ctx in test_suite_list:
            test_v = test_ctx.accept(self)
            if test_v.value:
                return suite_ctx.accept(self)

    def visitTerm(self, ctx: goTolangParser.TermContext):
        child_len = ctx.getChildCount()
        if child_len == 1:
            return ctx.children[0].accept(self)
        # TODO long
        if ctx.STAR(0):
            # TODO type check
            left: CtxNode = ctx.children[0].accept(self)
            left_v = left.value
            right: CtxNode = ctx.children[2].accept(self)
            right_v = right.value
            return CtxNode(is_ptr=False, type="int", value=left_v * right_v, ctx=ctx)
        elif ctx.MOD(0):
            left: CtxNode = ctx.children[0].accept(self)
            left_v = left.value
            right: CtxNode = ctx.children[2].accept(self)
            right_v = right.value
            return CtxNode(is_ptr=False, type="int", value=left_v % right_v, ctx=ctx)

    def visitArith_expr(self, ctx: goTolangParser.Arith_exprContext):
        child_len = ctx.getChildCount()
        if child_len == 1:
            return ctx.children[0].accept(self)

        left: CtxNode = ctx.children[0].accept(self)

        for i in range(1, child_len, 2):
            # why None?
            right: CtxNode = ctx.children[i + 1].accept(self)
            if left.type != right.type:
                raise Exception("Can't calculate between different type {} and {}".format(left.type, right.type))

            # TODO QAQ so many todo
            if left.type == "int":
                if ctx.children[i].symbol.type == goTolangParser.ADD:
                    result_v = left.value + right.value
                    left = CtxNode(is_ptr=False, type="int", value=result_v, ctx=ctx)
                elif ctx.children[i].symbol.type == goTolangParser.MINUS:
                    result_v = left.value + right.value
                    left = CtxNode(is_ptr=False, type="int", value=result_v, ctx=ctx)
        return left

    def visitExpr_stmt(self, ctx: goTolangParser.Expr_stmtContext):
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)

        if ctx.ASSIGN(0):
            self.left = True
            left: CtxNode = ctx.testlist_star_expr(0).accept(self)
            self.left = False

            if not left.is_ptr:
                raise GoTolangSymbolCannotAssignError(left, ctx)
            right: CtxNode = ctx.testlist_star_expr(1).accept(self)
            # TODO 判断类型？
            left.cite.value = (right.type, right.value)
        elif ctx.augassign():
            left: CtxNode = ctx.testlist_star_expr(0).accept(self)

            AUG_ASSIGN: goTolangParser.AugassignContext = ctx.augassign()
            if not left.is_ptr:
                raise GoTolangSymbolCannotAssignError(left, ctx)
            right: CtxNode = ctx.testlist().accept(self)
            if AUG_ASSIGN.ADD_ASSIGN():
                left.cite.value = (left.cite.type, left.value + right.value)
            elif AUG_ASSIGN.SUB_ASSIGN():
                left.cite.value = (left.cite.type, left.value - right.value)

        return left
        # return CtxNode(is_ptr=True, type="cite", value=left.cite, ctx=ctx)

    def visitGoback_stmt(self, ctx: goTolangParser.Goback_stmtContext):
        label = int(ctx.NUMBER().getText())
        raise GobackException(label)

    def visitBto(self, ctx: goTolangParser.BtoContext):
        label = int(ctx.NUMBER().getText())
        self.env.last_goto[label].append(ctx)
        raise GotoException(label)

    def visitBif(self, ctx: goTolangParser.BifContext):
        label = int(ctx.NUMBER().getText())
        cond: CtxNode = ctx.or_test().accept(self)
        if cond.value:
            self.env.last_goto[label].append(ctx)
            raise GotoException(label)
        else:
            return None

    def visitAtom_expr(self, ctx: goTolangParser.Atom_exprContext):
        atom: goTolangParser.AtomContext = ctx.atom()
        atom_ctx_node: CtxNode = atom.accept(self)
        trailer_ctx_nodes: List[CtxNode] = [tailer.accept(self) for tailer in ctx.trailer()]

        ret = atom_ctx_node
        for trailer_ctx_node in trailer_ctx_nodes:
            if trailer_ctx_node.type == "arg list":
                # TODO func param check
                args = trailer_ctx_node.value
                if not isinstance(ret.value, GoTolangFunc):
                    raise Exception("Error type")  # TODO
                try:
                    ret = ret.value(*(arg.cite if arg.is_ptr else arg.value for arg in args))
                except GoTolangRuntimeError as exc:
                    exc.ctx = ctx
                    raise exc
                ret.ctx = ctx
            elif trailer_ctx_node.type == "sub list":
                # TODO type check
                subs = trailer_ctx_node.value
                if not isinstance(ret.value, GoTolangArrayBase):
                    raise Exception("Error type")  # TODO
                ele_ptr = ret.value.get_ele(tuple(sub.value for sub in subs))
                ret = CtxNode(is_ptr=True, type="ele ele", value=ele_ptr, ctx=ctx)

        return ret

    def visitArglist(self, ctx: goTolangParser.ArglistContext):
        arg_list = tuple(arg_node.accept(self) for arg_node in ctx.argument())
        return CtxNode(is_ptr=False, type="arg list", value=arg_list, ctx=ctx)

    def visitSubscriptlist(self, ctx: goTolangParser.SubscriptlistContext):
        sub_list = tuple(sub_node.accept(self) for sub_node in ctx.subscript())
        return CtxNode(is_ptr=False, type="sub list", value=sub_list, ctx=ctx)

    def visitAtom(self, ctx: goTolangParser.AtomContext):
        if ctx.OPEN_PAREN() is not None:
            return ctx.testlist_comp().accept(self)
        if ctx.NAME():
            symbol = ctx.NAME().getText()

            # TODO
            if self.left:
                self.env.set_symbol_init(symbol, ctx)

            symbol_meta = self.env.get_symbol_meta(symbol, ctx)
            ctx_node = CtxNode(is_ptr=True, type="cite", value=symbol_meta, ctx=ctx)
        elif ctx.NUMBER():
            child = ctx.NUMBER()
            ctx_node = CtxNode(is_ptr=False, type="int", value=int(child.getText()), ctx=ctx)
        elif ctx.STRING():
            child = ctx.STRING()
            ctx_node = CtxNode(is_ptr=False, type="str", value=eval(child.getText()), ctx=ctx)
        elif ctx.BOOL_TRUE():
            ctx_node = CtxNode(is_ptr=False, type="bool", value=True, ctx=ctx)
        elif ctx.BOOL_FALSE():
            ctx_node = CtxNode(is_ptr=False, type="bool", value=False, ctx=ctx)
        else:
            raise Exception("Not Implement yet!")

        return ctx_node

    def visitComparison(self, ctx: goTolangParser.ComparisonContext):
        if not ctx.comp_op():
            return self.visitChildren(ctx)
        COMP_OP: goTolangParser.Comp_opContext = ctx.comp_op(0)
        left, right = [child.accept(self) for child in ctx.expr()]
        left_v, right_v = left.value, right.value

        if COMP_OP.LESS_THAN():
            result = (left_v < right_v)
        elif COMP_OP.LT_EQ():
            result = (left_v <= right_v)
        elif COMP_OP.GREATER_THAN():
            result = (left_v > right_v)
        elif COMP_OP.GT_EQ():
            result = (left_v >= right_v)
        elif COMP_OP.EQUALS():
            result = (left_v == right_v)
        elif COMP_OP.NOT_EQ_2():
            result = (left_v != right_v)
        else:
            result = False
        return CtxNode(is_ptr=False, type="bool", value=result, ctx=ctx)

    def visitChildren(self, node, begin_node=None):
        result = self.defaultResult()
        n = node.getChildCount()
        si = 0 if not begin_node else node.children.index(begin_node)

        for i in range(si, n):
            c = node.getChild(i)
            if not isinstance(c, Tree.TerminalNodeImpl):
                result = c.accept(self)

        return result

    @goto_resume
    def visitFile_input(self, ctx: goTolangParser.File_inputContext):
        pass

    @change_env
    @goto_resume
    def visitFile_input_no_eof(self, ctx: goTolangParser.File_input_no_eofContext):
        pass

    @goto_resume
    def visitStmt(self, ctx: goTolangParser.StmtContext):
        pass

    @goto_resume
    def visitSuite(self, ctx: goTolangParser.SuiteContext):
        pass

    @goto_resume
    def visitSimple_stmt(self, ctx: goTolangParser.Simple_stmtContext):
        pass

    @goto_resume
    def visitBlabel(self, ctx: goTolangParser.BlabelContext):
        pass

    @goto_resume
    def visitBgoto(self, ctx: goTolangParser.BgotoContext):
        pass
