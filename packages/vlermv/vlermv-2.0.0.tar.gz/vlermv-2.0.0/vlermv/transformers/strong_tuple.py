ERROR = TypeError('key must be a tuple of strings.')
def to_path(key):
    if not isinstance(key, tuple):
        raise ERROR
    for x in key:
        if not isinstance(x, str):
            raise ERROR
    return key

from .tuple import from_path
