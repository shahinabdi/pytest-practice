import pytest
from src.converter import CurrencyConverter

# TODO 7: Create a test class with related test cases


class TestCurrencyConverterGroup:
    """Group related test cases using pytest features

    Requirements:
    - Use at least one pytest.mark.parametrize within the class
    - Use the converter fixture
    - Create at least two test methods that are logically related
    - Use pytest.approx for float comparisons
    - Add proper test documentation
    """

    @pytest.mark.parametrize("amount,currency", [
        # Add test cases that make sense to group together
        # Example: (100, 'USD'), (200, 'EUR')
    ])
    def test_round_trip_conversion(self, converter, amount, currency):
        """Test converting currency back and forth results in original amount"""
        pass

    @pytest.mark.parametrize("conversions", [
        # Add sequences of conversions to test
        # Example: [('USD', 'EUR'), ('EUR', 'GBP'), ('GBP', 'USD')]
    ])
    def test_conversion_chain(self, converter, conversions):
        """Test a chain of conversions maintains reasonable accuracy"""
        pass
