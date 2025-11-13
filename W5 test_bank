from bank import value
import pytest

def test_value_return():
    assert value("hello")==0
    assert value("h")==20
    assert value("anything else")==100

def test_value_casesensitivity():
    assert value("HELLO")==0
    assert value("Hiya")==20
    assert value("what's going On")==100

def test_value_str():
    with pytest.raises(AttributeError):
        value(5)
