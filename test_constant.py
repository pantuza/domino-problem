from nose import with_setup

from domino import constant


def test_domino_with_correct_n_numbers():
    """ Compute domino with 7 numbers """
    assert constant(7) == 12, "Not ok"

def test_domino_with_0_numbers():
    """ Compute domino with 0 numbers """
    try:
        constant(0)
    except Exception as e:
        assert isinstance(e, ValueError)

def test_domino_with_1_numbers():
    """ Compute domino with 1 numbers """
    assert constant(1) == 0, "Not ok"

def test_domino_with_2_numbers():
    """ Compute domino with 2 numbers """
    assert constant(2) == 1, "Not ok"

def test_domino_with_3_numbers():
    """ Compute domino with 3 numbers """
    assert constant(3) == 2, "Not ok"

def test_domino_with_4_numbers():
    """ Compute domino with 4 numbers """
    assert constant(4) == 4, "Not ok"

def test_domino_with_9_numbers():
    """ Compute domino with 9 numbers """
    assert constant(9) == 20, "Not ok"

def test_domino_with_15_numbers():
    """ Compute domino with 15 numbers """
    assert constant(15) == 56, "Not ok"

def test_domino_with_42_numbers():
    """ Compute domino with 42 numbers """
    assert constant(42) == 441, "Not ok"
