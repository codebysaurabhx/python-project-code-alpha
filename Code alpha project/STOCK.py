# TASK 2: Stock Portfolio Tracker

def main():
    # Hardcoded dictionary to define stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 140,
        "MSFT": 400,
        "AMZN": 150
    }

    portfolio = {}
    
    print("=== Stock Portfolio Tracker ===")
    print("Available stocks:", ", ".join(stock_prices.keys()))
    print("Type 'done' when you are finished entering stocks.\n")

    # User inputs stock names and quantity
    while True:
        stock_name = input("Enter stock name (or 'done' to finish): ").upper()
        
        if stock_name == 'DONE':
            break
        
        if stock_name not in stock_prices:
            print(f"Error: {stock_name} is not in our database. Please choose from the available stocks.")
            continue
        
        try:
            quantity = int(input(f"Enter quantity for {stock_name}: "))
            if quantity < 0:
                print("Quantity cannot be negative. Please try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid integer for the quantity.")
            continue

        # Add to portfolio
        if stock_name in portfolio:
            portfolio[stock_name] += quantity
        else:
            portfolio[stock_name] = quantity

    # Calculate and display total investment value
    print("\n=== Portfolio Summary ===")
    report_lines = []
    report_lines.append(f"{'Stock':<10} | {'Quantity':<10} | {'Price':<10} | {'Total Value':<10}")
    report_lines.append("-" * 50)
    
    total_investment = 0.0
    
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        total_value = price * qty
        total_investment += total_value
        report_lines.append(f"{stock:<10} | {qty:<10} | ${price:<9} | ${total_value:<9}")

    report_lines.append("-" * 50)
    report_lines.append(f"Total Investment Value: ${total_investment}")

    report_text = "\n".join(report_lines)
    print(report_text)

    # Optionally save the result in a .txt file
    save_option = input("\nWould you like to save this portfolio report to a file? (yes/no): ").strip().lower()
    if save_option in ['yes', 'y']:
        filename = "portfolio_tracker_output.txt"
        try:
            with open(filename, 'w') as file:
                file.write(report_text)
            print(f"Success! Portfolio saved to {filename}.")
        except Exception as e:
            print(f"An error occurred while saving the file: {e}")

if __name__ == "__main__":
    main()
