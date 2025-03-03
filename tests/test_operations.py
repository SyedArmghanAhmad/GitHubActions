from src.math_operations import add, subtract

def test_add():
    assert add(3, 4) == 7
    assert add(-1, 5) == 4
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(7, 4) == 3
    assert subtract(-5, 1) == -6
    assert subtract(0, 0) == 0

