class NoMoreUndosException(Exception):
    def __init__(self, message = 'No more undos available!'):
        super().__init__(message)

class NoMoreRedosException(Exception):
    def __init__(self, message = 'No more redos available!'):
        super().__init__(message)
