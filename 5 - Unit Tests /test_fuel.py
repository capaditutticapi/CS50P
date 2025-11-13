import pytest
import fuel

def test_convert_values():
    assert fuel.convert("1/2") == 50
    assert fuel.convert("99/100") == 99
    assert fuel.convert("1/10") == 10

def test_convert_errors():
    with pytest.raises(ValueError):
        fuel.convert("3/2")
    with pytest.raises(ValueError):
        fuel.convert("-1/2")
    with pytest.raises(ValueError):
        fuel.convert("3/-4")
    with pytest.raises(ZeroDivisionError):
        fuel.convert("3/0")

def test_gauge():
    assert fuel.gauge(0) == "E"
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(100) == "F"
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(49) == "49%"
