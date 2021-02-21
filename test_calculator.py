"""
Unit tests for the calculator library
"""

import calculator


class TestCalculator:
    def test_addition(self):
        assert 12 == calculator.add(5, 7)

    def test_subtraction(self):
        assert 4 == calculator.substract(10, 6)
