class CurrencyConverter:
    """
    A class to convert amounts between different currencies.
    """
    def __init__(self):
        """
        Initializes the converter with a dictionary of exchange rates relative to USD.
        These rates are for demonstration purposes and should be updated
        with real-time data using an API for actual financial transactions.
        """
        self.rates = {
            'USD': 1.0,         # Base currency (Static)
            'EUR': 0.8497,      # 1 USD = 0.8497 EUR
            'JPY': 146.38,      # 1 USD = 146.38 JPY
            'CNY': 7.16,        # 1 USD = 7.16 CNY
            'GBP': 0.7386,      # 1 USD = 0.7386 GBP
        }
        self.symbols = {
            'USD': '$',
            'EUR': '€',
            'JPY': '¥',
            'CNY': '¥',
            'GBP': '£'
        }

    def convert(self, amount, from_currency, to_currency):
        """
        Converts an amount from one currency to another.
        """
        if from_currency not in self.rates or to_currency not in self.rates:
            print("Error: Invalid currency code provided.")
            return None

        # First, convert the 'from_currency' amount to USD (our base currency)
        amount_in_usd = amount / self.rates[from_currency]

        # Now, convert the USD amount to the 'to_currency'
        converted_amount = amount_in_usd * self.rates[to_currency]

        return converted_amount

    def display_currencies(self):
        """Prints the available currencies."""
        print("Available currencies:")
        for code in self.rates:
            print(f"- {code}")

def main():
    """
    Main function to run the currency converter application.
    """
    converter = CurrencyConverter()

    print("--- Welcome to the Python Currency Converter! ---")
    print("I can help you convert between different currencies.\n")

    converter.display_currencies()

    while True:
        try:
            # Get user input
            amount_str = input("\nEnter the amount to convert (or 'q' to quit): ")
            if amount_str.lower() == 'q':
                break

            amount = float(amount_str)
            from_currency = input("Enter the source currency (e.g., USD): ").upper()
            to_currency = input("Enter the target currency (e.g., EUR): ").upper()

            # Perform the conversion
            result = converter.convert(amount, from_currency, to_currency)

            if result is not None:
                from_symbol = converter.symbols.get(from_currency, from_currency)
                to_symbol = converter.symbols.get(to_currency, to_currency)
                print(f"\n--- Conversion Result ---")
                print(f"{from_symbol}{amount:,.2f} {from_currency} is equal to {to_symbol}{result:,.2f} {to_currency}")
                print("-------------------------")

        except ValueError:
            print("Oops! Please enter a valid number for the amount.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    print("\nThanks for using the currency converter. Have a great day!")

if __name__ == "__main__":
    main()