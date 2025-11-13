import sys
import requests
import json

def main():
    if len(sys.argv) == 2:
        try:
            n = float(sys.argv[1])
            print(f"${bitcoinprice(n):,.4f}")
        except(ValueError):
            sys.exit("Invalid command-line entry for number of Bitcoins")

    else:
        sys.exit("Invalid ammount of command line arguments")

def bitcoinprice(n):
    try:
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=9d76a6de4e04330088e87ec4e2877e5205243047c69fb8a0b483671fdc711b20")
    except(requests.HTTPError):
        sys.exit("couldn't complete request")

    info = response.json()
    dollars = float(info["data"]["priceUsd"])
    return n*dollars

if __name__ == "__main__":
    main()
