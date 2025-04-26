import pytest
from calculator import Calculator,PreciseCalculator

@pytest.mark.parametrize("a, b, expected",
                         [
                            (3, 5, 8),
                            (-1, 1, 0),
                            (-1, -1, -2),
                            (0, 0, 0)
                        ])

def test_add_parameterized(calculator,a, b, expected):
    assert calculator.add(a, b) == expected
    
@pytest.mark.parametrize("a,b, expected",[(2,6,12),(-4,-9,36),(-2.3,3.12,-7.176)])

def test_multiply_parameterized(calculator,a,b,expected):
    assert calculator.multiply(a,b) == pytest.approx(expected) #for floating point otherwise show error due to rounding of
    # assert calc.multiply(a, b) ==expected
    
@pytest.mark.parametrize("a,b, expected",[(2,6,-4),(-4,-9,5),(-2,3,-5)])

def test_subtract_parameterized(calculator,a,b,expected):
    assert calculator.subtract(a, b) ==expected
    
# def test_subtract():
#     calc = Calculator()
#     assert calc.subtract(5, 3) == 2
#     assert calc.subtract(1, 5) == -4
#     assert calc.subtract(-5, -3) == -2

# def test_multiply():
#     calc = Calculator()
#     assert calc.multiply(2,2) ==4
#     #pytest.approx() allows us to compare floats with a tolerance which makes our test more robust. that why the bug we added in the will not show error
#     #Because floating-point numbers can’t always be represented exactly in memory
#     assert calc.multiply(1.2, 2.2) == pytest.approx(2.64, rel=1e-2)
#     assert calc.multiply(3, 4.65) == pytest.approx(13.95, rel=1e-2)


@pytest.mark.parametrize("a,b, expected",[(6,2,3),(8,2,4),(9,4,2.25)])

def test_divide_parameterized(calculator,a,b,expected):
    assert calculator.divide(a,b) == expected
    

# def test_divide():
#     calc = Calculator()
#     assert calc.divide(4,2) == 2
#     assert calc.divide(5,2) == 2.5
#     assert calc.divide(7, 4) == pytest.approx(1.75)
#     assert calc.divide(6,0)
    
    
@pytest.mark.parametrize("a,b, expected",[(2,2,4),(3,2,9),(4,2,16),(2, -2, 0.25), # Should be 1/(2^2) = 0.25
(10, -1, 0.1)]) # Should be 1/10 = 0.1])

def test_power_parameterized(calculator,a,b,expected):
    assert calculator.power(a,b) == expected
    
    
# @pytest.mark.parametrize("a,expected",[(0,0),(-1,ValueError("Fibonacci is not defined for negative numbers")),(2,1),(3,2)])

# def test_fibonacci(calculator,a,expected):
#     assert calculator.fibonacci(a) == expected

# @pytest.mark.parametrize("a,expected",[(0,1),(1,1),(-2,ValueError("Error")),(3,6)])

# def test_factorial(calculator,a,expected):
#     assert calculator.factorial(a) == expected


#There are two of handling the negative number error 
#1) Create separate test function for negative values 
#2)This below method 
@pytest.mark.parametrize("a,expected", [
    (0, 1),
    (1, 1),
    (-2, ValueError),
    (3, 6)
])
def test_factorial(calculator, a, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            calculator.factorial(a)
    else:
        assert calculator.factorial(a) == expected


@pytest.mark.parametrize("a,expected", [
    (0, 0),
    (1, 1),
    (-1, ValueError),
    (3, 2)
])
def test_fibonacci(calculator, a, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            calculator.fibonacci(a)
    else:
        assert calculator.fibonacci(a) == expected


def test_precise_addition(precise_calculator):
    result = precise_calculator.add(1.1234, 2.5678)
    assert result == 3.69
    
def test_precise_subtraction(precise_calculator):
    result = precise_calculator.subtract(5.6789, 2.1234)
    assert result == 3.56
    
def test_precise_multiplication(precise_calculator):
    result = precise_calculator.multiply(1.234, 2.345)
    assert result == 2.89

def test_precise_division(precise_calculator):
    result = precise_calculator.divide(5.6789, 2.1234)
    assert result == 2.67

def test_precise_power(precise_calculator):
    result = precise_calculator.power(2.345, 2)
    assert result == 5.5
    
def test_fibonacci(precise_calculator):
    assert precise_calculator.fibonacci(5) == 5
    assert precise_calculator.fibonacci(7) == 13
    assert precise_calculator.fibonacci(10) == 55


def test_factorial(precise_calculator):
    assert precise_calculator.factorial(5) == 120
    assert precise_calculator.factorial(7) == 5040
    assert precise_calculator.factorial(0) == 1
    
    
    
 
@pytest.mark.parametrize("precision,a,b,expected", [
    (2, 5.6789, 2.1234, 3.56),
    (3, 5.6789, 2.1234, 3.556),
    (1, 5.6789, 2.1234, 3.6),
])
def test_precise_subtraction_with_various_precisions(precision, a, b, expected):
    calc = PreciseCalculator(precision=precision)
    assert calc.subtract(a, b) == pytest.approx(expected, rel=1e-2)

    
@pytest.mark.parametrize("precision,a,b,expected", [
    (2, 2.345, 2, 5.5),
    (3, 2.345, 2, 5.502),
    (1, 2.345, 2, 5.5),
])
def test_precise_power_with_various_precisions(precision, a, b, expected):
    calc = PreciseCalculator(precision=precision)
    assert calc.power(a, b) == pytest.approx(expected, rel=1e-2)

    
@pytest.mark.parametrize("precision,a,b,expected", [
    (2, 5.6789, 2.1234, 2.67),
    (3, 5.6789, 2.1234, 2.674),
    (1, 5.6789, 2.1234, 2.7),
])
def test_precise_division_with_various_precisions(precision, a, b, expected):
    calc = PreciseCalculator(precision=precision)
    assert calc.divide(a, b) == expected
    
@pytest.mark.parametrize("precision,a,b,expected", [
    (2, 1.234, 2.345, 2.89),
    (3, 1.234, 2.345, 2.894),
    (1, 1.234, 2.345, 2.9),
])
def test_precise_multiplication_with_various_precisions(precision, a, b, expected):
    calc = PreciseCalculator(precision=precision)
    assert calc.multiply(a, b) == expected