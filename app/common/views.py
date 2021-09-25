import json

from django.views import View
from django.http import JsonResponse

from app.common.base.errors import Errors
from app.common.base.exceptions import BasicException
from app.common.base.handlers import request_handler


class BaseView(View):
    def __init__(self):
        super().__init__()
        self.requestData = None
        self.responseData = None
        self.setCookie = dict()
        self.code = Errors.SUCCESS
        self.message = Errors.getMessage(self.code)

    def setCode(self, code=0):
        self.code = code

    def setMessage(self, message=''):
        self.message = message

    def getCode(self):
        return self.code

    def getMessage(self):
        return self.message

    def assembleResponse(self, data=None, **kwargs):
        if self.responseData is None or type(self.requestData) != dict:
            self.responseData = dict()

        self.responseData['code'] = self.getCode()
        self.responseData['message'] = self.getMessage()

        if data:
            self.responseData['data'] = data
        if kwargs:
            self.responseData.update(kwargs)

        return self.responseData

    def responseJson(self, httpStatus=200, safe=False, **kwargs):

        if not self.responseData:
            self.assembleResponse()

        responseObject = JsonResponse(self.responseData, status=httpStatus, safe=safe)

        if self.setCookie:
            for cookieKey, cookieValue in self.setCookie.items():
                responseObject.set_cookie(cookieKey, cookieValue)

        return responseObject


class TestView(BaseView):

    @request_handler()
    def get(self, request):
        return 'django server is running'


