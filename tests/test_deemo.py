from app.deemo import add, subtract, multiply, divide
import pytest

#skip decorator
# @pytest.mark.skip("Arbitrary skip")

def test_add():
    assert add(10, 20) == 30

def test_subtract():
    assert subtract(30, 20) == 10

def test_multiply():
    assert multiply(10, 20) == 200

def test_divide():
    assert divide(100, 20) == 5
    #case for asserting exceptions
    with pytest.raises(ValueError):
        divide(4, 0)