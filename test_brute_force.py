from nose import with_setup

from domino import build_matrix
from domino import brute_force


def compute(n):
    matrix = build_matrix(n)
    total = brute_force(matrix)
    return total


def test_domino_with_correct_n_numbers():
    """ Compute domino with 7 numbers """
    assert compute(7) == 12, "Not ok"

def test_domino_with_0_numbers():
    """ Compute domino with 0 numbers """
    try:
        compute(0)
    except Exception as e:
        assert isinstance(e, ValueError)

def test_domino_with_1_numbers():
    """ Compute domino with 1 numbers """
    assert compute(1) == 0, "Not ok"

def test_domino_with_2_numbers():
    """ Compute domino with 2 numbers """
    assert compute(2) == 1, "Not ok"

def test_domino_with_3_numbers():
    """ Compute domino with 3 numbers """
    assert compute(3) == 2, "Not ok"

def test_domino_with_4_numbers():
    """ Compute domino with 4 numbers """
    assert compute(4) == 4, "Not ok"

def test_domino_with_9_numbers():
    """ Compute domino with 9 numbers """
    assert compute(9) == 20, "Not ok"

def test_domino_with_15_numbers():
    """ Compute domino with 15 numbers """
    assert compute(15) == 56, "Not ok"

def test_domino_with_42_numbers():
    """ Compute domino with 42 numbers """
    assert compute(42) == 441, "Not ok"
