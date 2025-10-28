import pytest
from source import check_robot_status

test_cases = [
    # --- Biến R, C ---
    ((0, 1, 10, []), "NOT OK"),
    ((2, 4, 10, []), "NOT OK"),
    ((2, 4, 10, []), "NOT OK"),
    ((1, 3, 10, []), "OK"),
    ((1, 3, 10, [(1, 3)]), "NOT OK"),
    ((1, 3, 10, [(1, 2)]), "OK"),

    # --- Biến energy ---
    ((1, 3, 10, [(1, 3)]), "NOT OK"),
    ((1, 3, 9, [(1, 3)]), "NEED CHARGING"),
    ((1, 3, 10, [(1, 3)]), "NOT OK"),
    ((1, 3, 19, [(1, 2), (2, 2)]), "NEED CHARGING"),
    ((1, 3, 20, [(1, 2), (1, 3)]), "NOT OK"),

    # --- Biến obstacles ---
    ((1, 3, 9, [(1, 3)]), "NEED CHARGING"),
    ((1, 3, 9, []), "OK"),
    ((1, 3, 10, [(1, 3)]), "NOT OK"),
    ((1, 3, 10, [(1, 2)]), "OK"),

    # --- Biến i ---
    ((1, 3, 10, [(1, 2)]), "OK"),
    ((1, 3, 10, [(1, 2)]), "OK"),
    ((1, 3, 9, []), "OK"),
    ((1, 3, 10, [(1, 3)]), "NOT OK"),
    ((1, 3, 10, [(1, 2)]), "OK"),
    ((1, 3, 19, [(1, 2), (2, 2)]), "NEED CHARGING"),
    ((1, 3, 10, [(1, 2)]), "OK"),
    ((1, 3, 20, [(1, 2), (1, 3)]), "NOT OK"),
]

@pytest.mark.parametrize("inputs, expected", test_cases)
def test_check_robot_status(inputs, expected):
    R, C, energy, obstacles = inputs
    assert check_robot_status(R, C, energy, obstacles) == expected
