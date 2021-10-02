import shlex
from contextlib import suppress
from typing import List, Dict, Union, Iterable, Tuple, Any

import pydantic
from pydantic import BaseModel

from tasker_schemas import MatchAliasRule


class classer:
    def __init__(self, target):
        self.target = target

    def filter(self, request):
        if isinstance(request, list):
            pass
        if isinstance(request, dict):
            pass


def from_str__to__pytype(inp_val: str) -> Any:
    import json
    if inp_val in 'True true ok on'.split():
        out_val = True
    elif inp_val in 'False false fail off'.split():
        out_val = False
    elif inp_val in 'None null'.split():
        out_val = False
    else:
        out_val = json.loads(inp_val)
    return out_val


class ExtractResult(BaseModel):
    name: str
    val_str: str
    row: List[str]

    @property
    def value(self):
        return from_str__to__pytype(self.val_str)


def _extradite_tokens_segments(
        line_arr: List[str],
        token_to_alias_map: Dict[str, Union[dict, MatchAliasRule]],
) -> Iterable[ExtractResult]:

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
                if rule.nplaces == 1:
                    value = 'True'
                elif rule.nplaces == 2:
                    value = row[1]
                else:
                    value = row
                yield ExtractResult(name=name, val_str=value, row=row)


def extradite_tokens_segments(
        line_arr: List[str],
        token_to_alias_map: Dict[str, Union[dict, MatchAliasRule]],
) -> Dict[str, ExtractResult]:
    """ Extracts aliases from lists
    Args:
        line_arr: list of strings
        token_to_alias_map: rules for extraction by match to alias
        places: number of places of interest on the right side

    Returns: generator of names

    """
    items_exp = _extradite_tokens_segments(line_arr, token_to_alias_map)
    res = {it.name: it for it in items_exp}
    return res


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