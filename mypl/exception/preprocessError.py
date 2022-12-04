
class goTolangPreError(BaseException):
    def __init__(self):
        pass


class duplicatedLabelError(goTolangPreError):
    def __init__(self, label, ctx):
        pass
