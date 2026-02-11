import pytest
from jar import Jar

def test_init():
    jar = Jar() #creating the object
    assert jar.capacity == 12
    jar2 = Jar(5)
    assert jar2.capacity == 5


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(2)
    assert jar.size == 2
    jar.deposit(5)
    assert jar.size == 7


def test_withdraw():
    jar = Jar()
    jar.deposit(8)
    assert jar.size == 8
    jar.withdraw(4)
    assert jar.size == 4
    jar.withdraw(2)
    assert jar.size == 2
