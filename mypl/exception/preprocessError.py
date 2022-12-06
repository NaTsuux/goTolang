from .baseError import GoTolangBaseError


class GoTolangPreError(GoTolangBaseError):
    def __init__(self, ctx):
        super(GoTolangPreError, self).__init__(ctx)


class DuplicatedLabelError(GoTolangPreError):
    def __init__(self, ctx):
        super(DuplicatedLabelError, self).__init__(ctx)


class LongComparisonError(GoTolangPreError):
    def __init__(self, ctx):
        super(LongComparisonError, self).__init__(ctx)
