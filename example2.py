def add(a, b):
    return a + b


def test_add():
    #assert add(0.1,0.2)==approx(0.3)
    assert add(0.1, 0.2) -0.3 <1.0e-6
