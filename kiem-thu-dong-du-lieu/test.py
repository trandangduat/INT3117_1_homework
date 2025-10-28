import pytest
from source import check_robot_status

test_cases = [
    # --- Biến R, C ---
    ((0, 1, 10, []), "NOT OK"),                   # (1, 2)(T)
    ((2, 4, 10, []), "NOT OK"),                   # (1, 2)(F)
    ((2, 4, 10, []), "NOT OK"),                   # (1, 4)(T)
    ((1, 3, 10, []), "OK"),                       # (1, 4)(F)
    ((1, 3, 10, [(1, 3)]), "NOT OK"),             # (1, 11)(T)
    ((1, 3, 10, [(1, 2)]), "OK"),                 # (1, 11)(F)

    # --- Biến energy ---
    ((1, 3, 10, [(1, 3)]), "NOT OK"),             # (1, 10)(T)
    ((1, 3, 9, [(1, 3)]), "NEED CHARGING"),       # (1, 8)(T)
    ((1, 3, 10, [(1, 2)]), "OK"),                 # (1, 8)(F)
    ((1, 3, 19, [(1, 2), (2, 2)]), "NEED CHARGING"), # (10, 8)(T)
    ((1, 3, 20, [(1, 2), (1, 3)]), "NOT OK"),     # (10, 8)(F)

    # --- Biến obstacles ---
    ((1, 3, 9, [(1, 3)]), "NEED CHARGING"),       # (1, 7)(T)
    ((1, 3, 9, []), "OK"),                        # (1, 7)(F)
    ((1, 3, 10, [(1, 3)]), "NOT OK"),             # (1, 11)(T)
    ((1, 3, 10, [(1, 2)]), "OK"),                 # (1, 11)(F)

    # --- Biến i ---
    ((1, 3, 10, [(1, 3)]), "OK"),                 # (6, 13)(T)
    ((1, 3, 10, [(1, 2)]), "OK"),                 # (6, 7)(T)
    ((1, 3, 9, [(1, 3)]), "NEED CHARGING"),       # (6, 7)(F)
    ((1, 3, 10, [(1, 3)]), "NOT OK"),             # (6, 11)(T)
    ((1, 3, 10, [(1, 2)]), "OK"),                 # (6, 11)(F)

    # --- Lặp khi có nhiều obstacles ---
    ((1, 3, 19, [(1, 2), (2, 2)]), "NEED CHARGING"), # (13, 7)(T)
    ((1, 3, 10, [(1, 2)]), "OK"),                 # (13, 7)(F)
    ((1, 3, 20, [(1, 2), (1, 3)]), "NOT OK"),     # (13, 11)(T)
    ((1, 3, 10, [(1, 2)]) ,"OK"),                # (13, 11)(F)
]

@pytest.mark.parametrize("inputs, expected", test_cases)
def test_check_robot_status(inputs, expected):
    R, C, energy, obstacles = inputs
    assert check_robot_status(R, C, energy, obstacles) == expected
