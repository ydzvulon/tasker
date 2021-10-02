import shlex
from contextlib import suppress
from typing import List, Dict, Union, Iterable, Tuple, Any

import pydantic

from tasker.tasker_schemas import MatchAliasRule


def parse_to_line(text: str):
    list_items = shlex.split(text.strip())


def extradite_tokens_segments(
        line_arr: List[str],
        token_to_alias_map: Dict[str, Union[dict, MatchAliasRule]],
) -> Iterable[Tuple[str, List[str]]]:
    """ Extracts aliases from lists
    Args:
        line_arr: list of strings
        token_to_alias_map: rules for extraction by match to alias
        places: number of places of interest on the right side

    Returns: generator of names

    """
    for name, _rule in token_to_alias_map.items():
        if isinstance(_rule, dict):
            rule = MatchAliasRule(**_rule)
        else:
            rule = _rule

        for alias in rule.aliases:
            striped = alias.strip()
            if striped in line_arr:
                idx = line_arr.index(striped)
                row = list(line_arr[idx: idx + rule.nplaces])
                line_arr.remove(striped)
                yield name, row


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