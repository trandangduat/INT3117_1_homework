import pytest
from source import check_robot_cleaning

obstacles = [(3, 3), (4, 5)]

@pytest.mark.parametrize("R,C,obstacles,expected", [
    (0, 2, [(3, 3), (4, 5)], "NOT OK"),
    (1, 6, [(3, 3), (4, 5)], "NOT OK"),
    (3, 6, [], "OK"),
    (3, 4, [(3, 3)], "OK"),
    (3, 3, [(3, 3)], "NOT OK"),
])
def test_check_robot_status(R, C, obstacles, expected):
    result = check_robot_cleaning(R, C, obstacles)
    assert result == expected