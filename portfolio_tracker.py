import csv
import datetime

from main import save_to_csv


def portfolio_tracker():
    """Stock Portfolop Tracker with hardcoded prices and CSV export."""

    # Hardcoded stock prices
    stock_prices = {
        "AAPL": 180.50,
        "TSLA": 450.75,
        "GOOGL": 135.20,
        "MSFT": 340.90,
        "AMZN": 145.30,
        "NVDA": 450.80,
        "META": 305.65,
        "NFLX": 400.25
    }

    portfolio = []  # List to store portfolio holdings
    total_investment = 0.0  # Variable to track total investment

    print("=== STOCK PORTFOLIO TRACKER ===")
    print("Available stocks and prices:")
    for stock, price in stock_prices.items():
        print(f"  {stock}: ${price: .2f}")
    print()

    while True:
        try:
            # Get stock input
            stock_input = input(
                "Enter stock symbol (or 'done' to finish, 'list' for prices, 'show' for portfolio): "
            ).upper().strip()

            if stock_input == 'DONE':
                break
            elif stock_input == 'LIST':
                print("\nAvaliable stocks and prices:")
                for stock, price in stock_prices.items():
                    print(f"  {stock}: ${price: .2f}")
                continue
            elif stock_input == 'SHOW':
                if portfolio:
                    print("\n=== CURRENT PORTFOLIO ===")
                    # Aggregate holdings by stock
                    aggregated = {}
                    for holding in portfolio:
                        stock = holding['stock']
                        if stock in aggregated:
                            aggregated[stock]['quantity'] += holding[
                                'quantity']
                            aggregated[stock]['total'] += holding['total']
                        else:
                            aggregated[stock] = {
                                'qantity': holding['quantity'],
                                'price': holding['price'],
                                'total': holding['total']
                            }

                    print(
                        f"{'Stock':<8} {'Qty':<6} {'Price':<10} {'Total':<12}")
                    print("-" * 36)
                    for stock, data in aggregated.items():
                        print(
                            f"{stock:<8} {data['quantity']:<6} ${data['price']:<9.2f} ${data['total']:<11.2f}"
                        )
                    print("-" * 36)
                    print(f"Total Investment: ${total_investment:.2f}\n")
                else:
                    print("\nYour portfolio is empty.\n")
                    continue

            if stock_input not in stock_prices:
                print(
                    f"Stock '{stock_input}' not available. Type 'list' to see available stocks."
                )
                continue

            # Get quantity input
            while True:
                try:
                    quantity = int(
                        input(f"Enter quantity for {stock_input}: "))
                    if quantity <= 0:
                        print("Please enter a positive number.")
                        continue
                    break
                except ValueError:
                    print("Please enter a valid number.")

            # Calculate investment for this stock
            stock_price = stock_prices[stock_input]
            stock_total = stock_price * quantity

            # Add to portfolio
            portfolio.append({
                "stock": stock_input,
                "quantity": quantity,
                "price": stock_price,
                "total": stock_total,
            })

            total_investment += stock_total
            print(
                f"Added {quantity} shares of {stock_input} at ${stock_price:.2f} each = ${stock_total:.2f}"
            )
            print(f" Current total investment: ${total_investment:.2f}\n")

        except KeyboardInterrupt:
            print("\nExiting portfolio tracker...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

    # Display final portfolio
    if portfolio:
        print("\n=== PORTFOLIO SUMMARY ===")
        print(f"{'Stock':<8} {'Qty':<6} {'Price':<10} {'Total':<12}")
        print("-" * 36)

        for holding in portfolio:
            print(
                f"{holding['stock']:<8} {holding['quantity']:<6} ${holding['price']:<9.2f} ${holding['total']:<11.2f}"
            )

        print("-" * 36)
        print(f"{'TOTAL INVESTMENT:':,26} ${total_investment:.2f}")

        # Ask if user wants to save to CSV
        save_choice = input(
            "\nSave portfolio to CSV file? (y/n):").lower().strip()
        if save_choice in ['y', 'yes']:
            save_to_csv(portfolio, total_investment)
    else:
        print("No stocks added to portfolio.")


def save_to_csv(portfolio, total_investment):
    """Save portfolio data to CSV file."""
    try:
        filename = f"portfolio_{datetime.now().strfttime('%Y%m%d_%H%M%S')}.csv"

        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['Stock', 'Quantity', 'Price', 'Total']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for holding in portfolio:
                writer.writerow({
                    'Stock': holding['stock'],
                    'Quantity': holding['quantity'],
                    'Price': holding['price'],
                    'Total': holding['total']
                })

            # Add total row
            writer.writerow({
                'Stock': 'TOTAL',
                'Quantity': '',
                'Price': '',
                'Total': total_investment
            })

        print(f"Portfolio saved to {filename}")

    except Exception as e:
        print(f"Error saving to CSV: {e}")


if __name__ == "__main__":
    portfolio_tracker()
