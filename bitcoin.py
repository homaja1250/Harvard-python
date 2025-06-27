import sys
import requests

def get_bitcoin_price():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
        return float(data["bpi"]["USD"]["rate_float"])
    except requests.RequestException:
        sys.exit("Error: Unable to get the current Bitcoin price.")

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python bitcoin.py <number_of_bitcoins>")

    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Error: Invalid number of Bitcoins.")

    price_per_bitcoin = get_bitcoin_price()
    total_cost = n * price_per_bitcoin
    print(f"The current cost of {n} Bitcoins is: ${total_cost:,.4f}")

if __name__ == "__main__":
    main()
