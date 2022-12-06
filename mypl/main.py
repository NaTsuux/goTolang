from antlr4 import FileStream, CommonTokenStream

from .base.env import GoTolangEnv
from .exception import GotoException, GoTolangPreError, goTolangRuntimeError
from .exception.gotoException import GobackException
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
    except GoTolangPreError as exc:
        print(exc.__traceback__)
        return
    main_visitor = goTolangMainVisitor(tree, env)

    label = (None, None)
    while True:
        try:
            main_visitor.run(*label)
            break
        except GotoException as exc:
            label = (exc.label, None)
        except GobackException as exc:
            label = (None, exc.label)
        except goTolangRuntimeError as exc:
            print(exc.__repr__())
            return

    print("\n==========================")
    print(main_visitor.env)
