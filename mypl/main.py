from antlr4 import FileStream, CommonTokenStream

from .gen import *
from .goTolangPreVisitor import goTolangPreVisitor
from .goTolangMainVisitor import goTolangMainVisitor
from .exception import GotoException


def run_file(input_stream: FileStream):
    lexer = goTolangLexer(input_stream)  # (StdinStream())
    stream = CommonTokenStream(lexer)
    parser = goTolangParser(stream)
    tree = parser.file_input()
    visitor = goTolangPreVisitor(tree)
    main_visitor = goTolangMainVisitor(tree)

    resume_path = []
    while True:
        try:
            main_visitor.my_visit(resume_path)
            break
        except GotoException as exc:
            resume_path = visitor.label_d.get(exc.label)

    print(visitor.label_d)
    print(main_visitor.symbol_d)
