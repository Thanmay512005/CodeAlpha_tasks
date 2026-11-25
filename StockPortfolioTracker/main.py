def main():
    # Sample stock prices in US dollars.
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 140,
        "MSFT": 420,
        "AMZN": 190
    }

    portfolio = {}

    print("Stock Portfolio Tracker")
    print("\nAvailable stocks:")
    for stock, price in stock_prices.items():
        print(f"{stock}: ${price}")

    print("\nEnter a stock name and quantity.")
    print("Type 'done' when you have finished.\n")

    while True:
        stock_name = input("Stock name: ").upper().strip()

        if stock_name == "DONE":
            break

        if stock_name not in stock_prices:
            print("Stock not found. Please choose from the available list.")
            continue

        quantity_text = input("Quantity: ").strip()

        try:
            quantity = int(quantity_text)
            if quantity <= 0:
                print("Please enter a quantity greater than zero.")
                continue
        except ValueError:
            print("Please enter a whole number for the quantity.")
            continue

        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
        print("Stock added to your portfolio.\n")

    if not portfolio:
        print("\nNo stocks were added.")
        return

    print("\nYour portfolio:")
    total_investment = 0

    for stock, quantity in portfolio.items():
        stock_value = stock_prices[stock] * quantity
        total_investment += stock_value
        print(f"{stock}: {quantity} shares x ${stock_prices[stock]} = ${stock_value}")

    print(f"\nTotal investment value: ${total_investment}")

    save_choice = input("\nSave this summary to a text file? (yes/no): ").lower().strip()

    if save_choice == "yes":
        with open("portfolio_summary.txt", "w", encoding="utf-8") as file:
            file.write("Stock Portfolio Summary\n")
            for stock, quantity in portfolio.items():
                stock_value = stock_prices[stock] * quantity
                file.write(f"{stock}: {quantity} shares = ${stock_value}\n")
            file.write(f"\nTotal investment value: ${total_investment}\n")

        print("Summary saved as portfolio_summary.txt.")


if __name__ == "__main__":
    main()
