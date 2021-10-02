import shlex

from pytest_steps import test_steps

from struct_utils import extradite_tokens_segments
from tasker_schemas import MatchAliasRule


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