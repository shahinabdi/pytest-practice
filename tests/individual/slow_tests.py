import pytest
import time


@pytest.mark.slow
class TestCurrencyConverterSlow:
    """Tests that might take longer to execute"""

    @pytest.mark.parametrize("amount", [
        10**i for i in range(1, 8)  # Test with increasingly large numbers
    ])
    def test_large_number_conversion(self, converter, amount):
        """Test conversion with increasingly large numbers"""
        result = converter.convert(amount, 'USD', 'JPY')
        assert isinstance(result, float)
        assert result == pytest.approx(amount * 110.0)

    def test_multiple_currency_chain(self, converter):
        """Test long chain of currency conversions"""
        amount = 1000
        currencies = ['USD', 'EUR', 'GBP', 'JPY',
                      'AUD'] * 20  # Multiple conversions

        current_amount = amount
        for i in range(len(currencies) - 1):
            current_amount = converter.convert(
                current_amount,
                currencies[i],
                currencies[i + 1]
            )
            time.sleep(0.1)  # Simulate slow operation

        assert isinstance(current_amount, float)

    @pytest.mark.parametrize("precision", range(1, 11))
    def test_high_precision_calculations(self, converter, precision):
        """Test conversions with increasing decimal precision"""
        amount = 1.0 / (10 ** precision)
        result = converter.convert(amount, 'USD', 'EUR')
        expected = amount * 0.85
        assert result == pytest.approx(expected, rel=1e-10)
        time.sleep(0.1)  # Simulate slow operation
