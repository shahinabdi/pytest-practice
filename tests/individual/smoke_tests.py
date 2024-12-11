import pytest


@pytest.mark.smoke
class TestCurrencyConverterSmoke:
    """Quick smoke tests to verify basic functionality works"""

    def test_usd_to_eur_conversion(self, converter):
        """Verify basic USD to EUR conversion works"""
        result = converter.convert(100, 'USD', 'EUR')
        assert result == 85.00

    def test_eur_to_usd_conversion(self, converter):
        """Verify basic EUR to USD conversion works"""
        result = converter.convert(100, 'EUR', 'USD')
        assert result == pytest.approx(117.65)

    def test_basic_error_handling(self, converter):
        """Verify basic error handling works"""
        with pytest.raises(ValueError):
            converter.convert(-100, 'USD', 'EUR')

    def test_get_last_result(self, converter):
        """Verify last result tracking works"""
        converter.convert(100, 'USD', 'EUR')
        assert converter.get_last_conversion() == 85.00
