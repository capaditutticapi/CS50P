import pytest
from plates import is_valid

def test_is_valid_starts():
    assert is_valid("aaaa22") == True
    assert is_valid("22aaaa") == False

def test_is_valid_length():
    assert is_valid("a") == False
    assert is_valid("aaaaaaa") == False
    assert is_valid("aaa") == True

def test_is_valid_middlenumber():
    assert is_valid("AAA22A") == False
    assert is_valid("AAA222") == True

def test_is_valid_zero():
    assert is_valid("aaaa00") == False
    assert is_valid("aa01") == False
    assert is_valid("aaa100") == True
    assert is_valid("aa10") == True

def test_is_valid_speciaslcharacter():
    assert is_valid("aaaa!") == False
    assert is_valid("aaa10.") == False
