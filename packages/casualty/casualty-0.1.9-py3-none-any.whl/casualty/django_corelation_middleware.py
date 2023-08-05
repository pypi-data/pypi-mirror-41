import uuid

import structlog

from casualty.casualty_logger import configure_structlog
from casualty.constants import HTTP_REQUEST_HEADER



def setup_request_id(request):
    logger = structlog.getLogger()
    if request.META.get(HTTP_REQUEST_HEADER):
        current_request_id = request.META.get(HTTP_REQUEST_HEADER)

    else:
        current_request_id = str(uuid.uuid4())
    logger = logger.bind(request_id=current_request_id)




class DjangoCorelationMiddleware(object):
    """
    If request_id header is present bind it to logger
    else create an ew request_id and bind it to logger
    It uses
    """

    def __init__(self, get_response):
        self.get_response = get_response
        if not structlog.is_configured():
            configure_structlog()

    def __call__(self, request):
        setup_request_id(request)

        response = self.get_response(request)

        return response


class DjangoCorelationOldMiddleware(object):
    """
    If request_id header is present bind it to logger
    else create an ew request_id and bind it to logger
    It uses
    """

    def __init__(self):
        if not structlog.is_configured():
            configure_structlog()

    def process_request(self, request):
        setup_request_id(request)