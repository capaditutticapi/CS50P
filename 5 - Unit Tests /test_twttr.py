import pytest
from twttr import shorten

def test_shorten_upper():
    assert shorten("HELLO WORLD") == "HLL WRLD"
    assert shorten("AEIOU") == ""

def test_shorten_lower():
    assert shorten ("hello weird world") == "hll wrd wrld"
    assert shorten ("aeiou") == ""

def test_shorten_numbers():
    assert shorten("H3ll0 W31rd W0rld") == "H3ll0 W31rd W0rld"

def test_shorten_punctuation():
    assert shorten("Hello! weird! world! :)") == "Hll! wrd! wrld! :)"
