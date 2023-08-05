__all__ = [
    "DojoError",
]


class DojoError(Exception):
    """Every Dojo-Exception inherits this class.
    """

    def __init__(self, message):
        self.message = message

    def __repr__(self):
        return self.message
