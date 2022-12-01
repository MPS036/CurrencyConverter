from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://free.currconv.com/"
API_KEY = ""

printer = PrettyPrinter()


def get_currencies():
    endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()['results']
    data = list(data.items())
    data.sort()
    return data


def print_currencies(currencies):
    for name, currency in currencies:
        name = currency['currencyName']
        _id = currency['id']
        symbol = currency.get("currencySymbol", "")
        print(f"{_id} - {name} - {symbol}")


def exchange_rate(cur1, cur2):
    endpoint = f"api/v7/convert?q={cur1}_{cur2}&compact=ultra&apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()
    if len(data) == 0:
        print('Invalid currencies')
        return
    rate = list(data.values())[0]
    print(f"{cur1} -> {cur2} = {rate}")
    return rate


def convert(cur1, cur2, amount):
    rate = exchange_rate(cur1, cur2)
    if rate is None:
        return
    try:
        amount = float(amount)
    except:
        print("Invalid amount")
        return
    converted_amount = rate * amount
    print(f"{amount} {cur1} is equal to {converted_amount} {cur2}")
    return converted_amount


def main():
    currencies = get_currencies()
    print("Hello! Type List to get the list with all the currencies, Convert to convert from one to another and Rate to get the exchange rate of two currencies")
    print()
    while True:
        command = input("Enter a command (q to quit)").lower()
        if command == "q":
            break
        elif command == "list":
            print_currencies(currencies)
        elif command == "convert":
            cur1 = input("Enter a currency you have: ").upper()
            amount = input(f"Enter an amount in {cur1}: ")
            cur2 = input("Enter a currency you want to get: ").upper()
            convert(cur1, cur2, amount)
        elif command == "rate":
            cur1 = input("Enter a currency you have: ").upper()
            cur2 = input("Enter a currency to convert to: ").upper()
            exchange_rate(cur1, cur2)
        else:
            print("Unrecognized command")


main()