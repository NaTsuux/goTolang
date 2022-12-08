# Generated from C:/Users/NaTsuu/pl\goTolang.g4 by ANTLR 4.11.1
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .goTolangParser import goTolangParser
else:
    from goTolangParser import goTolangParser


# This class defines a complete listener for a parse tree produced by goTolangParser.
class goTolangListener(ParseTreeListener):

    # Enter a parse tree produced by goTolangParser#file_input.
    def enterFile_input(self, ctx: goTolangParser.File_inputContext):
        pass

    # Exit a parse tree produced by goTolangParser#file_input.
    def exitFile_input(self, ctx: goTolangParser.File_inputContext):
        pass

    # Enter a parse tree produced by goTolangParser#file_input_no_eof.
    def enterFile_input_no_eof(self, ctx: goTolangParser.File_input_no_eofContext):
        pass

    # Exit a parse tree produced by goTolangParser#file_input_no_eof.
    def exitFile_input_no_eof(self, ctx: goTolangParser.File_input_no_eofContext):
        pass

    # Enter a parse tree produced by goTolangParser#stmt.
    def enterStmt(self, ctx: goTolangParser.StmtContext):
        pass

    # Exit a parse tree produced by goTolangParser#stmt.
    def exitStmt(self, ctx: goTolangParser.StmtContext):
        pass

    # Enter a parse tree produced by goTolangParser#simple_stmt.
    def enterSimple_stmt(self, ctx: goTolangParser.Simple_stmtContext):
        pass

    # Exit a parse tree produced by goTolangParser#simple_stmt.
    def exitSimple_stmt(self, ctx: goTolangParser.Simple_stmtContext):
        pass

    # Enter a parse tree produced by goTolangParser#Bexpr.
    def enterBexpr(self, ctx: goTolangParser.BexprContext):
        pass

    # Exit a parse tree produced by goTolangParser#Bexpr.
    def exitBexpr(self, ctx: goTolangParser.BexprContext):
        pass

    # Enter a parse tree produced by goTolangParser#Bpass.
    def enterBpass(self, ctx: goTolangParser.BpassContext):
        pass

    # Exit a parse tree produced by goTolangParser#Bpass.
    def exitBpass(self, ctx: goTolangParser.BpassContext):
        pass

    # Enter a parse tree produced by goTolangParser#Bgoback.
    def enterBgoback(self, ctx: goTolangParser.BgobackContext):
        pass

    # Exit a parse tree produced by goTolangParser#Bgoback.
    def exitBgoback(self, ctx: goTolangParser.BgobackContext):
        pass

    # Enter a parse tree produced by goTolangParser#Bgoto.
    def enterBgoto(self, ctx: goTolangParser.BgotoContext):
        pass

    # Exit a parse tree produced by goTolangParser#Bgoto.
    def exitBgoto(self, ctx: goTolangParser.BgotoContext):
        pass

    # Enter a parse tree produced by goTolangParser#Blabel.
    def enterBlabel(self, ctx: goTolangParser.BlabelContext):
        pass

    # Exit a parse tree produced by goTolangParser#Blabel.
    def exitBlabel(self, ctx: goTolangParser.BlabelContext):
        pass

    # Enter a parse tree produced by goTolangParser#Bto.
    def enterBto(self, ctx: goTolangParser.BtoContext):
        pass

    # Exit a parse tree produced by goTolangParser#Bto.
    def exitBto(self, ctx: goTolangParser.BtoContext):
        pass

    # Enter a parse tree produced by goTolangParser#Bif.
    def enterBif(self, ctx: goTolangParser.BifContext):
        pass

    # Exit a parse tree produced by goTolangParser#Bif.
    def exitBif(self, ctx: goTolangParser.BifContext):
        pass

    # Enter a parse tree produced by goTolangParser#label_stmt.
    def enterLabel_stmt(self, ctx: goTolangParser.Label_stmtContext):
        pass

    # Exit a parse tree produced by goTolangParser#label_stmt.
    def exitLabel_stmt(self, ctx: goTolangParser.Label_stmtContext):
        pass

    # Enter a parse tree produced by goTolangParser#expr_stmt.
    def enterExpr_stmt(self, ctx: goTolangParser.Expr_stmtContext):
        pass

    # Exit a parse tree produced by goTolangParser#expr_stmt.
    def exitExpr_stmt(self, ctx: goTolangParser.Expr_stmtContext):
        pass

    # Enter a parse tree produced by goTolangParser#testlist_star_expr.
    def enterTestlist_star_expr(self, ctx: goTolangParser.Testlist_star_exprContext):
        pass

    # Exit a parse tree produced by goTolangParser#testlist_star_expr.
    def exitTestlist_star_expr(self, ctx: goTolangParser.Testlist_star_exprContext):
        pass

    # Enter a parse tree produced by goTolangParser#augassign.
    def enterAugassign(self, ctx: goTolangParser.AugassignContext):
        pass

    # Exit a parse tree produced by goTolangParser#augassign.
    def exitAugassign(self, ctx: goTolangParser.AugassignContext):
        pass

    # Enter a parse tree produced by goTolangParser#pass_stmt.
    def enterPass_stmt(self, ctx: goTolangParser.Pass_stmtContext):
        pass

    # Exit a parse tree produced by goTolangParser#pass_stmt.
    def exitPass_stmt(self, ctx: goTolangParser.Pass_stmtContext):
        pass

    # Enter a parse tree produced by goTolangParser#goback_stmt.
    def enterGoback_stmt(self, ctx: goTolangParser.Goback_stmtContext):
        pass

    # Exit a parse tree produced by goTolangParser#goback_stmt.
    def exitGoback_stmt(self, ctx: goTolangParser.Goback_stmtContext):
        pass

    # Enter a parse tree produced by goTolangParser#if_stmt.
    def enterIf_stmt(self, ctx: goTolangParser.If_stmtContext):
        pass

    # Exit a parse tree produced by goTolangParser#if_stmt.
    def exitIf_stmt(self, ctx: goTolangParser.If_stmtContext):
        pass

    # Enter a parse tree produced by goTolangParser#suite.
    def enterSuite(self, ctx: goTolangParser.SuiteContext):
        pass

    # Exit a parse tree produced by goTolangParser#suite.
    def exitSuite(self, ctx: goTolangParser.SuiteContext):
        pass

    # Enter a parse tree produced by goTolangParser#or_test.
    def enterOr_test(self, ctx: goTolangParser.Or_testContext):
        pass

    # Exit a parse tree produced by goTolangParser#or_test.
    def exitOr_test(self, ctx: goTolangParser.Or_testContext):
        pass

    # Enter a parse tree produced by goTolangParser#and_test.
    def enterAnd_test(self, ctx: goTolangParser.And_testContext):
        pass

    # Exit a parse tree produced by goTolangParser#and_test.
    def exitAnd_test(self, ctx: goTolangParser.And_testContext):
        pass

    # Enter a parse tree produced by goTolangParser#not_test.
    def enterNot_test(self, ctx: goTolangParser.Not_testContext):
        pass

    # Exit a parse tree produced by goTolangParser#not_test.
    def exitNot_test(self, ctx: goTolangParser.Not_testContext):
        pass

    # Enter a parse tree produced by goTolangParser#comparison.
    def enterComparison(self, ctx: goTolangParser.ComparisonContext):
        pass

    # Exit a parse tree produced by goTolangParser#comparison.
    def exitComparison(self, ctx: goTolangParser.ComparisonContext):
        pass

    # Enter a parse tree produced by goTolangParser#comp_op.
    def enterComp_op(self, ctx: goTolangParser.Comp_opContext):
        pass

    # Exit a parse tree produced by goTolangParser#comp_op.
    def exitComp_op(self, ctx: goTolangParser.Comp_opContext):
        pass

    # Enter a parse tree produced by goTolangParser#expr.
    def enterExpr(self, ctx: goTolangParser.ExprContext):
        pass

    # Exit a parse tree produced by goTolangParser#expr.
    def exitExpr(self, ctx: goTolangParser.ExprContext):
        pass

    # Enter a parse tree produced by goTolangParser#xor_expr.
    def enterXor_expr(self, ctx: goTolangParser.Xor_exprContext):
        pass

    # Exit a parse tree produced by goTolangParser#xor_expr.
    def exitXor_expr(self, ctx: goTolangParser.Xor_exprContext):
        pass

    # Enter a parse tree produced by goTolangParser#and_expr.
    def enterAnd_expr(self, ctx: goTolangParser.And_exprContext):
        pass

    # Exit a parse tree produced by goTolangParser#and_expr.
    def exitAnd_expr(self, ctx: goTolangParser.And_exprContext):
        pass

    # Enter a parse tree produced by goTolangParser#shift_expr.
    def enterShift_expr(self, ctx: goTolangParser.Shift_exprContext):
        pass

    # Exit a parse tree produced by goTolangParser#shift_expr.
    def exitShift_expr(self, ctx: goTolangParser.Shift_exprContext):
        pass

    # Enter a parse tree produced by goTolangParser#arith_expr.
    def enterArith_expr(self, ctx: goTolangParser.Arith_exprContext):
        pass

    # Exit a parse tree produced by goTolangParser#arith_expr.
    def exitArith_expr(self, ctx: goTolangParser.Arith_exprContext):
        pass

    # Enter a parse tree produced by goTolangParser#term.
    def enterTerm(self, ctx: goTolangParser.TermContext):
        pass

    # Exit a parse tree produced by goTolangParser#term.
    def exitTerm(self, ctx: goTolangParser.TermContext):
        pass

    # Enter a parse tree produced by goTolangParser#factor.
    def enterFactor(self, ctx: goTolangParser.FactorContext):
        pass

    # Exit a parse tree produced by goTolangParser#factor.
    def exitFactor(self, ctx: goTolangParser.FactorContext):
        pass

    # Enter a parse tree produced by goTolangParser#power.
    def enterPower(self, ctx: goTolangParser.PowerContext):
        pass

    # Exit a parse tree produced by goTolangParser#power.
    def exitPower(self, ctx: goTolangParser.PowerContext):
        pass

    # Enter a parse tree produced by goTolangParser#atom_expr.
    def enterAtom_expr(self, ctx: goTolangParser.Atom_exprContext):
        pass

    # Exit a parse tree produced by goTolangParser#atom_expr.
    def exitAtom_expr(self, ctx: goTolangParser.Atom_exprContext):
        pass

    # Enter a parse tree produced by goTolangParser#atom.
    def enterAtom(self, ctx: goTolangParser.AtomContext):
        pass

    # Exit a parse tree produced by goTolangParser#atom.
    def exitAtom(self, ctx: goTolangParser.AtomContext):
        pass

    # Enter a parse tree produced by goTolangParser#testlist_comp.
    def enterTestlist_comp(self, ctx: goTolangParser.Testlist_compContext):
        pass

    # Exit a parse tree produced by goTolangParser#testlist_comp.
    def exitTestlist_comp(self, ctx: goTolangParser.Testlist_compContext):
        pass

    # Enter a parse tree produced by goTolangParser#trailer.
    def enterTrailer(self, ctx: goTolangParser.TrailerContext):
        pass

    # Exit a parse tree produced by goTolangParser#trailer.
    def exitTrailer(self, ctx: goTolangParser.TrailerContext):
        pass

    # Enter a parse tree produced by goTolangParser#subscriptlist.
    def enterSubscriptlist(self, ctx: goTolangParser.SubscriptlistContext):
        pass

    # Exit a parse tree produced by goTolangParser#subscriptlist.
    def exitSubscriptlist(self, ctx: goTolangParser.SubscriptlistContext):
        pass

    # Enter a parse tree produced by goTolangParser#testlist.
    def enterTestlist(self, ctx: goTolangParser.TestlistContext):
        pass

    # Exit a parse tree produced by goTolangParser#testlist.
    def exitTestlist(self, ctx: goTolangParser.TestlistContext):
        pass

    # Enter a parse tree produced by goTolangParser#arglist.
    def enterArglist(self, ctx: goTolangParser.ArglistContext):
        pass

    # Exit a parse tree produced by goTolangParser#arglist.
    def exitArglist(self, ctx: goTolangParser.ArglistContext):
        pass

    # Enter a parse tree produced by goTolangParser#subscript.
    def enterSubscript(self, ctx: goTolangParser.SubscriptContext):
        pass

    # Exit a parse tree produced by goTolangParser#subscript.
    def exitSubscript(self, ctx: goTolangParser.SubscriptContext):
        pass

    # Enter a parse tree produced by goTolangParser#argument.
    def enterArgument(self, ctx: goTolangParser.ArgumentContext):
        pass

    # Exit a parse tree produced by goTolangParser#argument.
    def exitArgument(self, ctx: goTolangParser.ArgumentContext):
        pass


del goTolangParser
