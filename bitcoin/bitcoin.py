import requests
import sys

def main():
    if len(sys.argv) != 2:
        print("Missing Command-line argument")
        sys.exit
    else:
        try:
            number = float(sys.argv[1])
            print(f"Argument received: {number}")
        except ValueError:
            print("Command-line argument is not a number")
            sys.exit
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = response.json()
    rate = data["bpi"]["USD"]["rate_float"]
    amount = number * rate
    print(f"${amount:,.4f}")


if __name__ == "__main__":
    main()
