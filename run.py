from antlr4 import FileStream, StdinStream
from mypl import run_file

src = """\
a=1
goto 10
a=a+1
->10
"""


if __name__ == '__main__':
    run_file(FileStream("inputs/goto1.txt", 'utf-8'))
