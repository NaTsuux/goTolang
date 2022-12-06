from antlr4 import FileStream, CommonTokenStream

from .base.env import GoTolangEnv
from .exception import GotoException, goTolangPreError, goTolangRuntimeError
from .gen import *
from .goTolangMainVisitor import goTolangMainVisitor
from .goTolangPreVisitor import goTolangPreVisitor


def run_file(input_stream: FileStream):
    lexer = goTolangLexer(input_stream)  # (StdinStream())
    stream = CommonTokenStream(lexer)
    parser = goTolangParser(stream)
    tree = parser.file_input()
    env = GoTolangEnv()
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

    print("==========================")
    print(main_visitor.env)
