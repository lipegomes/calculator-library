"""
Unit tests for the calculator library
"""

import calculator


class TestCalculator:
    def test_addition(self):
        assert 12 == calculator.add(5, 7)

    def test_subtraction(self):
        assert 4 == calculator.substract(10, 6)

    def test_multiplication(self):
        assert 10 == calculator.multiplication(1, 10)

    def test_division(self):
        assert 25 == calculator.division(100, 4)
