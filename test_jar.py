
import pytest
from jar import Jar

def test_jar_init():
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0

def test_jar_str():
    jar = Jar(10)
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

def test_jar_deposit():
    jar = Jar(10)
    jar.deposit(5)
    assert jar.size == 5

def test_jar_withdraw():
    jar = Jar(10)
    jar.deposit(5)
    jar.withdraw(3)
    assert jar.size == 2

def test_jar_capacity():
    jar = Jar(10)
    assert jar.capacity == 10

def test_jar_size():
    jar = Jar(10)
    assert jar.size == 0

def test_jar_invalid_capacity():
    with pytest.raises(ValueError):
        Jar(-1)

def test_jar_invalid_deposit():
    jar = Jar(10)
    with pytest.raises(ValueError):
        jar.deposit(-1)

def test_jar_invalid_withdraw():
    jar = Jar(10)
    with pytest.raises(ValueError):
        jar.withdraw(-1)

def test_jar_exceed_capacity():
    jar = Jar(10)
    with pytest.raises(ValueError):
        jar.deposit(11)

def test_jar_zero_capacity():
    with pytest.raises(ValueError):
        Jar(0)

def test_jar_zero_deposit():
    jar = Jar(10)
    with pytest.raises(ValueError):
        jar.deposit(0)

def test_jar_zero_withdraw():
    jar = Jar(10)
    jar.deposit(5)
    with pytest.raises(ValueError):
        jar.withdraw(0)


def test_jar_multiple_deposits():
    jar = Jar(10)
    jar.deposit(3)
    jar.deposit(4)
    assert jar.size == 7

def test_jar_multiple_withdraws():
    jar = Jar(10)
    jar.deposit(7)
    jar.withdraw(3)
    jar.withdraw(2)
    assert jar.size == 2

if __name__ == "__main__":
    pytest.main([__file__, "--exit-zero"])

