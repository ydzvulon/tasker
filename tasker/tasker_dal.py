from typing import Any
from loguru import logger
from contextlib import suppress


def safe_get(key, obj, default=None) -> Any:
    """
    Safely retrieve key from object
    Args:
        obj: Any. target object
        key: inner object adders token
        default: value to return on failure
    Returns:
        on success: value of requested key
        on failure default on failure
    PyDocTests
    >>> safe_get("str-val", 'some-key', "nop")
    nop
    >>> safe_get(1, [33,44,55,66], default="sdf")

    """
    res = default
    _primitives_ = (bool, int, float, str)
    if obj is None or isinstance(obj, _primitives_):
        # skip primitives
        res = default
    elif isinstance(key, int) and isinstance(obj, list):
        # return list item by index
        if 0 <= key < len(obj):
            res = obj[key]
    elif isinstance(obj, dict):
        # return dict item by key
        res = obj.get(key, default)
    elif hasattr(obj, 'get'):
        with suppress(Exception):
            res = obj.get(key)
    elif isinstance(key, str) and hasattr(obj, key):
        res = getattr(obj, key)
    else:
        with suppress(Exception):
            res = obj[key]
    return res


def test__safe_get():
    wi
    expected = 55
    actual = safe_get(2, [33, 44, 55, 66], default="sdf")
    assert actual == expected

