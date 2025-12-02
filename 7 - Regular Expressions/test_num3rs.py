from numb3rs import validate
import pytest

def test_validate_ips():
    assert validate("255.255.255.255")==True
    assert validate("512.512.512.512")==False
    assert validate("1.2.3.1000")==False
    assert validate("192.168.001.1")==False

def test_validate_strs():
    assert validate("cat")==False
    assert validate("dog")==False
