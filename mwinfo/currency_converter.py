import yaml
import importlib.resources

class CurrencyConverter:
    def __init__(self):
        # Load rates from YAML
        with importlib.resources.open_text("mwinfo.data", "currency_rates.yml", encoding="utf-8") as f:
            data = yaml.safe_load(f)
            self.base_currency = data["base_currency"]
            self.rates = data["rates"]

    def convert(self, amount, from_currency, to_currency):
        """Convert from one currency to another"""
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        # Convert amount to base currency first if needed
        if from_currency == self.base_currency:
            amount_in_base = amount
        else:
            rate_from = self.rates.get(from_currency)
            if not rate_from:
                raise ValueError(f"Unsupported currency: {from_currency}")
            amount_in_base = amount / rate_from

        # Convert from base currency to target
        if to_currency == self.base_currency:
            return amount_in_base
        else:
            rate_to = self.rates.get(to_currency)
            if not rate_to:
                raise ValueError(f"Unsupported currency: {to_currency}")
            return amount_in_base * rate_to
