import requests

API_KEY = "fca_live_y5v0V97pgvgdw20DrneiTHffj7ePCjh7hSZQaMi8"
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"
CURRENCIES = ["TRY", "EUR", "USD", "GBP", "AUD", "JPY", "RUB", "THB"]


def get_currencies(currency):
    currencies = ",".join(CURRENCIES)
    URL = f"{BASE_URL}&currencies={currencies}&base_currency={currency}"
    r = requests.get(URL)
    assert r.status_code == 200
    data = r.json()
    return data["data"]


if __name__ == '__main__':
    while True:
        base = input("Which currency you need to convert? (Q for quit): ").upper()
        if base == "Q":
            break
        else:
            amount = input("Money amount (Q for quit): ").upper()
            if amount == "Q":
                break
            else:
                try:
                    if base in CURRENCIES:
                        response = get_currencies(base)
                        response.pop(base)
                        response.update({n: float(amount) * response[n] for n in response.keys()})
                        print(response)
                    else:
                        print("invalid currency")
                except ValueError:
                    print("amount needs to be integer")
