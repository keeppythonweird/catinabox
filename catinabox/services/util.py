import functools
import json

import nameko.web.handlers


def http(*args, **kwargs):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            ret = func(*args, **kwargs)
            if isinstance(ret, tuple) and ret[1]:
                return ret[0], json.dumps(ret[1])
            else:
                return ret
        return nameko.web.handlers.http(*args, **kwargs)(wrapper)
    return decorator
