def check_robot_position2(R, C):
    if R < 1 or R > 5 or C < 1 or C > 7:
        return "NOT OK"
    if (1 <= R <= 2) and (4 <= C <= 7):
        return "NOT OK"
    return "OK"

import pytest

@pytest.mark.parametrize("R,C,expected", [
    (0,2,"NOT OK"),
    (1,6,"NOT OK"),
    (3,2,"OK"),
])
def test_robot(R,C,expected):
    assert check_robot_position2(R,C) == expected
