# Currency conversion rates (as per example)
conversion_rates = {
    "USD": 83.0,     # 1 USD = 83 INR
    "EUR": 90.0,     # 1 EUR = 90 INR
    "GBP": 105.0,    # 1 GBP = 105 INR
    "JPY": 0.57,     # 1 JPY = 0.57 INR
}

def convert_currency(amount, from_currency, to_currency):
    if from_currency not in conversion_rates or to_currency not in conversion_rates:
        return None
    # Convert from 'from_currency' to INR
    inr_amount = amount * conversion_rates[from_currency]
    # Convert INR to 'to_currency'
    converted = inr_amount / conversion_rates[to_currency]
    return round(converted, 2)

print("       💱 Currency Converter (Base: INR)")
print("Available currencies:", ", ".join(conversion_rates.keys()))

while True:
    from_curr = input("\nFrom Currency (USD/EUR/GBP/JPY): ").upper()
    to_curr = input("To Currency (USD/EUR/GBP/JPY): ").upper()

    try:
        amount = float(input(f"Enter amount in {from_curr}: "))
        result = convert_currency(amount, from_curr, to_curr)
        if result:
            print(f"{amount} {from_curr} = {result} {to_curr}")
        else:
            print("❌ Invalid currency entered.")
    except ValueError:
        print("❌ Please enter a valid number.")

    again = input("Convert again? (y/n): ").lower()
    if again != 'y':
        break