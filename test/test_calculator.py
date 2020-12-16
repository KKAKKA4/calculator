def test_add(calculator):
    assert calculator.add(1, 2) == 3
    assert calculator.add(2, 2) == 4

def test_subtract(calculator):
    assert calculator.subtract(5, 1) == 4
    assert calculator.subtract(3, 2) == 1

def test_multiply(calculator):
    assert calculator.multiply(2, 2) == 4
    assert calculator.multiply(5, 6) == 30
    
def test_divide(calculator):
    assert calculator.divide(2, 2) == 4
    assert calculator.divde(5, 6) == 30
    assert calculator.divde(5, 0) == None

def test_square(calculator):
    assert calculator.square(2) == 4
    assert calculator.square(5) == 25