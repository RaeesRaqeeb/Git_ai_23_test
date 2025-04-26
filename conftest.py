# conftest.py
import pytest
from calculator import Calculator,PreciseCalculator


@pytest.fixture
def calculator():
    return Calculator()

@pytest.fixture
def precise_calculator():
    return PreciseCalculator(precision=2)
