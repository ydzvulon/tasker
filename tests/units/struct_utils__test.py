from pytasker.struct_utils import safe_get


def test__safe_get():
    expected = 55
    actual = safe_get(2, [33, 44, 55, 66], default="sdf")
    assert actual == expected

