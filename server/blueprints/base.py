import logging
from functools import wraps

from flask import jsonify
from werkzeug.exceptions import HTTPException


def json_endpoint(f):
    @wraps(f)
    def json_decorator(*args, **kwargs):
        try:
            body, status = f(*args, **kwargs)
            response = jsonify(body)
            return response, status
        except Exception as e:
            response = jsonify(message=e.description if isinstance(e, HTTPException) else str(e))
            logging.getLogger().exception(response)
            response.status_code = 500
            return response

    return json_decorator
