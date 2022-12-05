from antlr4 import FileStream, CommonTokenStream

from .gen import *
from .goTolangPreVisitor import goTolangPreVisitor
from .goTolangMainVisitor import goTolangMainVisitor
from .goTolangEnv import goTolangEnv
from .exception import GotoException, goTolangPreError, goTolangRuntimeError


def run_file(input_stream: FileStream):
    lexer = goTolangLexer(input_stream)  # (StdinStream())
    stream = CommonTokenStream(lexer)
    parser = goTolangParser(stream)
    tree = parser.file_input()
    env = goTolangEnv()
    try:
        goTolangPreVisitor(tree, env).run()
    except goTolangPreError as exc:
        print(exc.__traceback__)
        return
    main_visitor = goTolangMainVisitor(tree, env)

    from_label = None
    while True:
        try:
            main_visitor.run(from_label)
            break
        except GotoException as exc:
            from_label = exc.label
        except goTolangRuntimeError as exc:
            print(repr(exc))
            return

    print(main_visitor.env)
