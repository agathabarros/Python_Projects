class MyCustomError(TypeError):
    """
    Exception raised when a specific error code is needed
    """
    def __init__(self, message, code):
        super().__init__(message)
        self.code = code

err = MyCustomError('an error', 500)
print(err.__doc__)