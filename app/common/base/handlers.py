import logging
import functools
import traceback

from app.common.base.errors import Errors
from app.common.base.exceptions import BasicException

logger = logging.getLogger('django')


def request_handler():
    def decorator(func):
        @functools.wraps(func)
        def wrapper(viewInstance, requestObject, *args, **kwargs):
            data = None
            try:
                data = func(viewInstance, requestObject, *args, **kwargs)

            except BasicException as e:
                logger.error(traceback.format_exc())
                viewInstance.setCode(e.code)
                viewInstance.setMessage(e.message)
                data = e.kwargs

            except:
                logger.error(traceback.format_exc())
                viewInstance.setCode(Errors.SEVER_ERROR)
                viewInstance.setMessage(Errors.getMessage(Errors.SEVER_ERROR))

            finally:
                viewInstance.assembleResponse(data)
                return viewInstance.responseJson()
        return wrapper
    return decorator

