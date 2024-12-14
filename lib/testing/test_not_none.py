from lib.bool_functions import return_not_none

def test_return_not_none():
    result = return_not_none()
    assert result is not None, "Expected a value, but got None."
