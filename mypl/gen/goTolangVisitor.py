# Generated from C:/Users/NaTsuu/pl\goTolang.g4 by ANTLR 4.11.1
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .goTolangParser import goTolangParser
else:
    from goTolangParser import goTolangParser


# This class defines a complete generic visitor for a parse tree produced by goTolangParser.

class goTolangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by goTolangParser#file_input.
    def visitFile_input(self, ctx: goTolangParser.File_inputContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by goTolangParser#file_input_no_eof.
    def visitFile_input_no_eof(self, ctx: goTolangParser.File_input_no_eofContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by goTolangParser#stmt.
    def visitStmt(self, ctx: goTolangParser.StmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by goTolangParser#simple_stmt.
    def visitSimple_stmt(self, ctx: goTolangParser.Simple_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by goTolangParser#Bexpr.
    def visitBexpr(self, ctx: goTolangParser.BexprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by goTolangParser#Bpass.
    def visitBpass(self, ctx: goTolangParser.BpassContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by goTolangParser#Bgoback.
    def visitBgoback(self, ctx: goTolangParser.BgobackContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by goTolangParser#Bgoto.
    def visitBgoto(self, ctx: goTolangParser.BgotoContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by goTolangParser#Blabel.
    def visitBlabel(self, ctx: goTolangParser.BlabelContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by goTolangParser#Bto.
    def visitBto(self, ctx: goTolangParser.BtoContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by goTolangParser#Bif.
    def visitBif(self, ctx: goTolangParser.BifContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by goTolangParser#label_stmt.
    def visitLabel_stmt(self, ctx: goTolangParser.Label_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by goTolangParser#expr_stmt.
    def visitExpr_stmt(self, ctx: goTolangParser.Expr_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by goTolangParser#testlist_star_expr.
    def visitTestlist_star_expr(self, ctx: goTolangParser.Testlist_star_exprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by goTolangParser#augassign.
    def visitAugassign(self, ctx: goTolangParser.AugassignContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by goTolangParser#pass_stmt.
    def visitPass_stmt(self, ctx: goTolangParser.Pass_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by goTolangParser#goback_stmt.
    def visitGoback_stmt(self, ctx: goTolangParser.Goback_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by goTolangParser#if_stmt.
    def visitIf_stmt(self, ctx: goTolangParser.If_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by goTolangParser#suite.
    def visitSuite(self, ctx: goTolangParser.SuiteContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by goTolangParser#or_test.
    def visitOr_test(self, ctx: goTolangParser.Or_testContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by goTolangParser#and_test.
    def visitAnd_test(self, ctx: goTolangParser.And_testContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by goTolangParser#not_test.
    def visitNot_test(self, ctx: goTolangParser.Not_testContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by goTolangParser#comparison.
    def visitComparison(self, ctx: goTolangParser.ComparisonContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by goTolangParser#comp_op.
    def visitComp_op(self, ctx: goTolangParser.Comp_opContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by goTolangParser#expr.
    def visitExpr(self, ctx: goTolangParser.ExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by goTolangParser#xor_expr.
    def visitXor_expr(self, ctx: goTolangParser.Xor_exprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by goTolangParser#and_expr.
    def visitAnd_expr(self, ctx: goTolangParser.And_exprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by goTolangParser#shift_expr.
    def visitShift_expr(self, ctx: goTolangParser.Shift_exprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by goTolangParser#arith_expr.
    def visitArith_expr(self, ctx: goTolangParser.Arith_exprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by goTolangParser#term.
    def visitTerm(self, ctx: goTolangParser.TermContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by goTolangParser#factor.
    def visitFactor(self, ctx: goTolangParser.FactorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by goTolangParser#power.
    def visitPower(self, ctx: goTolangParser.PowerContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by goTolangParser#atom_expr.
    def visitAtom_expr(self, ctx: goTolangParser.Atom_exprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by goTolangParser#atom.
    def visitAtom(self, ctx: goTolangParser.AtomContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by goTolangParser#testlist_comp.
    def visitTestlist_comp(self, ctx: goTolangParser.Testlist_compContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by goTolangParser#trailer.
    def visitTrailer(self, ctx: goTolangParser.TrailerContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by goTolangParser#subscriptlist.
    def visitSubscriptlist(self, ctx: goTolangParser.SubscriptlistContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by goTolangParser#testlist.
    def visitTestlist(self, ctx: goTolangParser.TestlistContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by goTolangParser#arglist.
    def visitArglist(self, ctx: goTolangParser.ArglistContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by goTolangParser#subscript.
    def visitSubscript(self, ctx: goTolangParser.SubscriptContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by goTolangParser#argument.
    def visitArgument(self, ctx: goTolangParser.ArgumentContext):
        return self.visitChildren(ctx)


del goTolangParser
