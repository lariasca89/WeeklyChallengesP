import requests

# 'currency' variable is the 3 letter code introduced by program user
# Get the current exchange rate


def expense_rate(currency):
    usd = requests.get('https://api.exchangerate-api.com/v4/latest/USD').json()
    rate = 1 / usd['rates'][currency]
    return rate


def amount_convert(rate, amount):
    amount_usd = []
    for value in amount:
        convert = value * rate
        amount_usd.append(convert)
    return amount_usd
