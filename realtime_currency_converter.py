import requests

class RealTimeCurrencyConverter:
    def __init__(self, url):
        self.url = url
        self.update_rates()

    def update_rates(self):
        try:
            # Get real-time exchange rates from the provided URL
            self.data = requests.get(self.url).json()
            # Extract currency rates from the data, using an empty dictionary as a default value
            self.currencies = self.data.get('rates', {})
        except requests.exceptions.RequestException:
            # Handle network errors and inform the user
            print("Failed to update currency rates due to a network error.")
            print("Please check your internet connection.")
            self.currencies = {}  # Set currencies to an empty dictionary in case of an error

    def convert(self, from_currency, to_currency, amount):
        if from_currency == to_currency:
            return amount  # No conversion needed for the same currency
        
        # Convert from the source currency to USD if it's not the base currency (USD)
        from_amount = amount / self.currencies[from_currency]

        # Perform the actual currency conversion to the target currency
        to_amount = from_amount * self.currencies[to_currency]

        # Round the result to 4 decimal places
        return round(to_amount, 4)

# Example usage:
converter = RealTimeCurrencyConverter('https://api.exchangerate-api.com/v4/latest/USD')
if __name__ == "__main__":
    print("Welcome to the Currency Converter!")

    while True:
        print("Currency list available for conversion: \n")
        print(list(converter.currencies.keys()),'\n')    
        fromcurrency = input("Enter the 'FROM' currency (or type 'exit' to quit): " ).upper().strip()
        # Check if the user wants to exit
        if fromcurrency == 'EXIT':
            break
        tocurrency = input("Enter the 'TO' currency: ").upper().strip()
        
        if fromcurrency not in converter.currencies and tocurrency not in converter.currencies:
            # Inform the user when both source and target currencies are not available
            print(f"ERROR : Currency '{fromcurrency}' and '{tocurrency}' are not available in the data.")
            continue

        if fromcurrency not in converter.currencies:
            # Inform the user when the source currency is not available
            print(f"ERROR : Currency '{fromcurrency}' is not available in the data.")
            continue

        if tocurrency not in converter.currencies:
            # Inform the user when the target currency is not available
            print(f"ERROR : Currency '{tocurrency}' is not available in the data.")
            continue
        
        try:
            amount = float(input("Enter the amount: "))
            if amount <= 0:
                # Inform the user when the amount is less than or equal to zero
                print("\u26A0 ERROR : Amount should be greater than Zero.")
            else:
                result = converter.convert(fromcurrency, tocurrency, amount)  # Call the conversion method
                if result is not None:
                    # Display the conversion result
                    print(f"{amount} {fromcurrency} is approximately {result} {tocurrency}")
        except ValueError:
            # Inform the user when an invalid input is provided
            print("\u26A0 ERROR : Invalid input. Enter a numeric value.")
