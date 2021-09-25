from app.common.base.errors import Errors


class BasicException(BaseException):

    def __init__(self, code=Errors.SEVER_ERROR, message=Errors.getMessage(Errors.SEVER_ERROR), **kwargs):
        self.code = code
        self.message = message
        self.kwargs = kwargs

