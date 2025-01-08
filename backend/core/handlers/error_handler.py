from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler


def error_handler(ext: Exception, context: dict):
    handlers = {
        'JWTException': _jwt_validation_exception_handler,

    }
    response = exception_handler(ext, context)
    ext_class = ext.__class__.__name__

    if ext_class in handlers:
        return handlers[ext_class](ext, context)

    return response


def _jwt_validation_exception_handler(ext, context):
    return Response({"detail": "JWT expired or invalid"}, status.HTTP_401_UNAUTHORIZED)
