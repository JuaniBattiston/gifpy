class GifpyBaseException(Exception):

    pass


class GifpyInvalidArgument(GifpyBaseException):
    def __init__(self):
        message = "Parameter is invalid"
        super().__init__(message)


class GifpyInvalidFormat(GifpyBaseException):
    def __init__(self):
        message = "The requested format was not found"
        super().__init__(message)


class GifpyFormatNotAvailable(GifpyBaseException):
    def __init__(self):
        message = "The requested format is not a valid format"
        super().__init__(message)
