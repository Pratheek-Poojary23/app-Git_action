from src.math_operation import add, sub, mul

def test_add():
    assert add(2,3) == 5
    assert add(-1,1) == 0

def test_sub():
    assert sub(5,3) == 2
    assert sub(10,4) == 6
    assert sub(0,5) == -5
    assert sub(-2,-3) == 1
    assert sub(5,0) == 5
    
def test_mul():
    assert mul(2,3) == 6
    assert mul(-1,1) == -1
    assert mul(0,5) == 0
    assert mul(-2,-3) == 6
    assert mul(5,0) == 0