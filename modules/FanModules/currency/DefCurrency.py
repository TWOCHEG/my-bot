import disnake
import json
from FluffBot import config

intents = disnake.Intents.default()
intents.members = True


def currency_add(user, amount):
    amount = int(amount)
    with open(config.CurrencyFile, 'r') as f:
        currency = json.load(f)

    if str(user.id) not in currency:
        currency[str(user.id)] = amount
    else:
        currency[str(user.id)] += amount

    with open(config.CurrencyFile, 'w') as f:
        json.dump(currency, f, indent=4)


def currency_remove(user, amount):
    amount = int(amount)
    with open(config.CurrencyFile, 'r') as f:
        currency = json.load(f)

    if str(user.id) not in currency:
        currency[str(user.id)] = amount
    else:
        currency[str(user.id)] -= amount

    with open(config.CurrencyFile, 'w') as f:
        json.dump(currency, f, indent=4)
