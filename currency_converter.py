def currency_converter(currency, amount, currency1):
    # Define exchange rates
    exchange_rates = {
        "USD_EUR": 0.87,
        "USD_JPY": 109.50,
        "USD_GBP": 0.72,
        "USD_AUD": 1.32,
        "USD_CAD": 1.24,
        "USD_CHF": 0.89,
        "USD_CNY": 6.43,
        "USD_SEK": 8.99,
        "USD_NZD": 1.42
    }

    # Convert currency if conversion exists
    if f"{currency}_{currency1}" in exchange_rates:
        rate = exchange_rates[f"{currency}_{currency1}"]
        converted_amount = float(amount) * rate
        return converted_amount
    else:
        return "Conversion not available"

def main():
    currency = input("Enter the currency you have: ")
    amount = input("Enter the amount you have: ")
    currency1 = input("Enter the currency you want to convert to: ")

    result = currency_converter(currency, amount, currency1)
    print(f"{amount} {currency} is equal to {result} {currency1}")

main()
