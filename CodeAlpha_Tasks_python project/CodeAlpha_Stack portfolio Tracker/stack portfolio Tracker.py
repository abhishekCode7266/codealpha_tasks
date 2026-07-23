# Hardcoded stock prices
stock_prices = {
    "APPLE": 180,
    "TSLA": 250,
    "GOOGLE": 140,
    "MSFT": 330,
    "AMZN": 135
}
                                                        
portfolio = {}
total_investment = 0

print("=" * 45)
print("       Stock Portfolio Tracker")
print("=" * 45)

while True:
    stock = input("Enter Stock Symbol (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        quantity = int(input("Enter Quantity: "))
        portfolio[stock] = quantity
    else:
        print("Stock not available!")

print("\n------ Portfolio Summary ------")

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment

    print(f"{stock} : {quantity} shares × ${price} = ${investment}")

print("-" * 35)
print(f"Total Investment Value = ${total_investment}")

# Save result to a text file (Optional)
with open("portfolio_report.txt", "w") as file:
    file.write("Stock Portfolio Report\n")
    file.write("-" * 30 + "\n")

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        investment = price * quantity
        file.write(f"{stock} : {quantity} shares × ${price} = ${investment}\n")

    file.write("-" * 30 + "\n")
    file.write(f"Total Investment Value = ${total_investment}")

print("\nPortfolio report saved as 'portfolio_report.txt'")