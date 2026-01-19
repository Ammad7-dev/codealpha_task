def stock_tracker():
    # 1. Hardcoded dictionary of stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 140,
        "MSFT": 370,
        "AMZN": 145
    }

    portfolio = []
    total_investment = 0

    print("--- Stock Portfolio Tracker ---")
    print("Available Stocks:", ", ".join(stock_prices.keys()))

    # 2. User Input Loop
    while True:
        symbol = input("\nEnter stock symbol (or type 'done' to finish): ").upper()
        
        if symbol == 'DONE':
            break
        
        if symbol in stock_prices:
            try:
                quantity = int(input(f"Enter quantity for {symbol}: "))
                price = stock_prices[symbol]
                holding_value = price * quantity
                
                # Store data in a dictionary
                portfolio.append({
                    "symbol": symbol,
                    "quantity": quantity,
                    "price": price,
                    "value": holding_value
                })
                total_investment += holding_value
                
            except ValueError:
                print("Invalid quantity. Please enter a number.")
        else:
            print("Stock symbol not found in our database.")

    # 3. Display Results
    print("\n--- Your Portfolio Summary ---")
    report_lines = ["Symbol | Quantity | Price | Total Value\n", "-" * 40 + "\n"]
    
    for item in portfolio:
        line = f"{item['symbol']:6} | {item['quantity']:8} | ${item['price']:4} | ${item['value']}\n"
        report_lines.append(line)
        print(line.strip())

    final_total = f"\nTotal Investment Value: ${total_investment}"
    print(final_total)
    report_lines.append(final_total)

    # 4. Save to File (Optional Task Requirement)
    save_choice = input("\nWould you like to save this report to a file? (y/n): ").lower()
    if save_choice == 'y':
        with open("portfolio_report.txt", "w") as f:
            f.writelines(report_lines)
        print("Report saved to 'portfolio_report.txt'!")

if __name__ == "__main__":
    stock_tracker()