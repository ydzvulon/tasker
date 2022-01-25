from typing import Optional

import pydantic
from pytest_steps import test_steps

class Foo(pydantic.BaseModel):
    bar: str = "text"
    met: Optional[bool]

@test_steps('stam sample')
def test_suite__extradite_tokens_segments():
    print("sf")
    assert bool is Foo.__fields__['met'].type_
    yield


def test_get_from_list():
    # arrange

    # act

    # assert
    assert True