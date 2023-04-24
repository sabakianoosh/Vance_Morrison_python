import factorial as f

def test_factorial():
    assert f.factorial(4)==24
    assert not f.factorial(5)==25
test_factorial()