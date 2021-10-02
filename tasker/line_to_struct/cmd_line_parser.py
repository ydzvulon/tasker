from dataclasses import dataclass
from typing import Dict, List, Union, Tuple, Iterable
import shlex

from pytest_steps import test_steps


@dataclass
class MatchAliasRule:
    nplaces: int
    aliases: List[str]


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
        if not isinstance(_rule, MatchAliasRule):
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



class MotionParser:

    def __init__(self, line: str):
        self.line_org = line
        self.line_arr = shlex.split(str)


@test_steps('extradite_tokens1', 'extradite_tokens2')
def test_suite__extradite_tokens_segments():
    print("@@act=declare block=step name=extradite_tokens_segments goal='keep'")
    cmd_arr = shlex.split("task -d ../.. ci-flow ci-publish -s --output prefixed")
    silent_extract = dict(
        silent=MatchAliasRule(nplaces=1, aliases=["-s", "--silent"]),
    )
    extracted = extradite_tokens_segments(cmd_arr, silent_extract)
    actual = dict(extracted)
    expected = {'silent': ['-s']}
    assert actual == expected
    yield

    print("@@act=declare block=step name=extradite_tokens_segments goal='keep'")
    cmd_arr = shlex.split("task -d ../.. ci-flow ci-publish -s --output prefixed")
    silent_extract = dict(
        si=dict(nplaces=1, aliases=["--si"])
    )
    extracted = extradite_tokens_segments(cmd_arr, silent_extract)
    actual = dict(extracted)
    expected = {}
    assert actual == expected
    yield