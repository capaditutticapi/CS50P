import pytest
from um import count


def test_count_correct():
    assert count("um I'm not sure, um...") == 2
    assert count(" um um um umumumum") == 3
    assert count("yummy um tummy um") == 2

def test_count_start_end():
    assert count("um um") == 2

def test_count_case_sensitivity():
    assert count("Um i um don't know.. UM..") == 3
    assert count("UM um Um hello") == 3

def test_count_within_words():
    with pytest.raises(SystemExit):
        count("yummy in my tummy")

