from jar import Jar
import pytest

def test_init():
    # Test the default capacity
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    # Test custom capacity
    jar = Jar(20)
    assert jar.capacity == 20
    assert jar.size == 0

    # Test invalid capacity (negative value)
    with pytest.raises(ValueError):
        jar = Jar(-5)

def test_str():
    jar = Jar()
    assert str(jar) == ""  # No cookies

    jar.deposit(1)
    assert str(jar) == "🍪"  # 1 cookie

    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"  # 12 cookies (full jar)

def test_deposit():
    jar = Jar(10)  
    jar.deposit(5)
    assert jar.size == 5

    jar.deposit(3)
    assert jar.size == 8

    # Test exceeding capacity
    with pytest.raises(ValueError):
        jar.deposit(3)

def test_withdraw():
    jar = Jar(10)
    jar.deposit(5)
    assert jar.size == 5

    jar.withdraw(2)
    assert jar.size == 3

    with pytest.raises(ValueError):
        jar.withdraw(4)
