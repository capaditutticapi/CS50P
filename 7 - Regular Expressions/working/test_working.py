import pytest
from working import convert

def test_convert_correct_times():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"

def test_convert_edge_cases():
    assert convert("12 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12 PM to 12:00 AM") == "12:00 to 00:00"

def test_convert_invalid_inputs():
    with pytest.raises(ValueError):
        convert("8:70 AM to 4:60 PM")
    with pytest.raises(ValueError):
        convert("8:75 to 13")
    with pytest.raises(ValueError):
        convert("12 5")
    with pytest.raises(ValueError):
        convert("14 to 13:68")
