class CurrencyConverter:
    """A simple currency converter"""

    RATES = {
        "USD": 1.0,
        "EUR": 0.85,
        "GBP": 0.75,
        "JPY": 110.0,
        "CAD": 1.25,
        "AUD": 1.35,
        "CHF": 0.92,
        "CNY": 6.75,
        "INR": 74.5,
    }

    def __init__(self):
        self.last_conversion = None

    def convert(self, amount: float, from_currency: str, to_currency: str) -> float:
        """
        Convert amount from one currency to another

        Args:
            amount: Amount to convert
            from_currency: Source currency code (e.g., 'USD')
            to_currency: Target currency code (e.g., 'EUR')

        Returns:
            float: Converted amount
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number")

        if amount < 0:
            raise ValueError("Amount cannot be negative")

        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if from_currency not in self.RATES:
            raise ValueError(f"Unsupported currency: {from_currency}")
        if to_currency not in self.RATES:
            raise ValueError(f"Unsupported currency: {to_currency}")

        # Convert to USD first
        usd_amount = amount / self.RATES[from_currency]
        # Then convert to target currency
        final_amount = usd_amount * self.RATES[to_currency]

        self.last_conversion = final_amount
        return round(final_amount, 2)

    def get_last_conversion(self) -> float:
        """Get the result of the last conversion"""
        if self.last_conversion is None:
            raise ValueError("No conversion has been performed yet")
        return self.last_conversion


if __name__ == "__main__":
    converter = CurrencyConverter()
    amount = float(input("Enter the amount to convert: "))
    from_currency = input("Enter the source currency code: ")
    to_currency = input("Enter the target currency code: ")

    try:
        result = converter.convert(amount, from_currency, to_currency)
        print(f"{amount} {from_currency} is equal to {result} {to_currency}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
