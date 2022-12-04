

class CtxNode:
    def __init__(self, is_ptr, type, value=None):
        self.is_ptr = is_ptr
        self.type = type
        self.value = value

    def set_value(self, value):
        self.value = value
