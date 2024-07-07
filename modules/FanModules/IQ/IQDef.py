import json
import random

from FluffBot import config


def iq(user):
    amount = random.randint(1, 200)

    amount = int(amount)
    with open(config.iq, 'r') as f:
        iq_user = json.load(f)

    if str(user.id) not in iq_user:
        iq_user[str(user.id)] = amount

    with open(config.iq, 'w') as f:
        json.dump(iq_user, f, indent=4)


def iq_add(user, amount):
    amount = int(amount)
    with open(config.iq, 'r') as f:
        currency = json.load(f)

    if str(user.id) not in currency:
        iq(user=user)
        currency[str(user.id)] += amount
    else:
        currency[str(user.id)] += amount

    with open(config.iq, 'w') as f:
        json.dump(currency, f, indent=4)


def iq_remove(user, amount):
    amount = int(amount)
    with open(config.iq, 'r') as f:
        currency = json.load(f)

    if str(user.id) not in currency:
        iq(user=user)
        currency[str(user.id)] -= amount
    else:
        currency[str(user.id)] -= amount

    with open(config.iq, 'w') as f:
        json.dump(currency, f, indent=4)
