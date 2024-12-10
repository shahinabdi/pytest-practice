import pytest
from src.converter import CurrencyConverter


@pytest.fixture
def converter():
    """Provide a fresh CurrencyConverter instance for each test"""
    return CurrencyConverter()


@pytest.fixture
def converter_with_history(converter):
    """Provide a converter with some conversion history"""
    converter.convert(100, 'USD', 'EUR')
    return converter


@pytest.fixture
def supported_currencies():
    """Provide list of supported currencies for tests"""
    return list(CurrencyConverter.RATES.keys())


def pytest_configure(config):
    """Register custom markers."""
    markers = [
        ("smoke", "mark test as smoke test (quick sanity check)"),
        ("slow", "mark test as slow running"),
        ("edge_cases", "mark tests that handle boundary and special cases"),
    ]
    for marker, help_text in markers:
        config.addinivalue_line("markers", f"{marker}: {help_text}")


@pytest.fixture
def verify_conversion():
    """Helper fixture to verify conversion results"""
    def _verify(amount, from_curr, to_curr, result):
        usd_amount = amount / CurrencyConverter.RATES[from_curr]
        expected = round(usd_amount * CurrencyConverter.RATES[to_curr], 2)
        assert result == pytest.approx(expected, rel=1e-2)
    return _verify
