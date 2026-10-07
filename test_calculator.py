from calculator import add, subtract
import pytest
@pytest.fixture
def calculate_numbers():
    return 10,5
def test_add(calculate_numbers):
    a, b = calculate_numbers
    assert a + b == 15

def test_subtract(calculate_numbers):
    a, b = calculate_numbers
    assert a - b == 5