import disnake
from disnake.ext import commands
import json
from FluffBot.modules.FanModules.currency.DefCurrency import currency_remove
from FluffBot import config


class SvShop(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_button_click(self, inter: disnake.MessageInteraction):
        user = inter.user
        if inter.component.custom_id not in ['ShopMAdmin', 'ShopLegenda', 'ShopEsh', 'ShopPedcarlik', 'ShopFem',
                                             'ShopGay', 'ShopSigma', 'ShopSigma']:
            return

        if inter.component.custom_id == 'ShopMAdmin':
            role = disnake.utils.get(inter.user.guild.roles, id=1257717919236751473)
            if role in inter.user.roles:
                await inter.send('у вас уже это есть', ephemeral=True)
                return
            with open('/FluffBot/modules/currency/currency.json', 'r') as f:
                currency = json.load(f)

            if str(user.id) in currency:
                current_balance = currency[str(user.id)]
                if current_balance < 40000:
                    await inter.send('кажется что у тебя нехватает баланса для этой покупки :(', ephemeral=True)
                    return
                elif current_balance > 40000:
                    currency_remove(user=user, amount=40000)
                    await user.add_roles(role)
                    await inter.send('отлично! ты один из немногих кто приобрел эту роль, можете этим гордится',
                                     ephemeral=True)

                    print(f'{config.consE}{inter.user} купил роль младшего админа')

        elif inter.component.custom_id == 'ShopLegenda':
            role = disnake.utils.get(inter.user.guild.roles, id=1155186958126022790)
            if role in inter.user.roles:
                await inter.send('у вас уже это есть', ephemeral=True)
                return
            user = inter.user
            with open('/FluffBot/modules/currency/currency.json', 'r') as f:
                currency = json.load(f)

            if str(user.id) in currency:
                current_balance = currency[str(user.id)]
                if current_balance < 5000:
                    await inter.send('кажется что у тебя нехватает баланса для этой покупки :(', ephemeral=True)
                    return
                elif current_balance > 5000:
                    currency_remove(user=user, amount=5000)
                    await user.add_roles(role)
                    await inter.send(
                        'отлично! ты купил роль олд/легенда, это конечно не самая лучшая роль но уже достижение',
                        ephemeral=True)

                    print(f'{config.consE}{inter.user} купил роль олд легенда')

        elif inter.component.custom_id == 'ShopCarlik':
            role = disnake.utils.get(inter.user.guild.roles, id=1256547016742273065)
            if role in inter.user.roles:
                await inter.send('у вас уже это есть', ephemeral=True)
                return
            user = inter.user
            with open('/FluffBot/modules/currency/currency.json', 'r') as f:
                currency = json.load(f)

            if str(user.id) in currency:
                current_balance = currency[str(user.id)]
                if current_balance < 1000:
                    await inter.send('кажется что у тебя нехватает баланса для этой покупки :(', ephemeral=True)
                    return
                elif current_balance > 1000:
                    currency_remove(user=user, amount=1000)
                    await user.add_roles(role)
                    await inter.send(
                        'отлично! ты купил эту роль',
                        ephemeral=True)

                    print(f'{config.consE}{inter.user} купил роль карлик')

        elif inter.component.custom_id == 'ShopSigma':
            role = disnake.utils.get(inter.user.guild.roles, id=1253712267745165352)
            if role in inter.user.roles:
                await inter.send('у вас уже это есть', ephemeral=True)
                return
            user = inter.user
            with open('/FluffBot/modules/currency/currency.json', 'r') as f:
                currency = json.load(f)

            if str(user.id) in currency:
                current_balance = currency[str(user.id)]
                if current_balance < 1000:
                    await inter.send('кажется что у тебя нехватает баланса для этой покупки :(', ephemeral=True)
                    return
                elif current_balance > 1000:
                    currency_remove(user=user, amount=1000)
                    await user.add_roles(role)
                    await inter.send(
                        'отлично! ты купил эту роль',
                        ephemeral=True)

                    print(f'{config.consE}{inter.user} купил роль сигма')

        elif inter.component.custom_id == 'ShopGay':
            role = disnake.utils.get(inter.user.guild.roles, id=1253434818125893784)
            if role in inter.user.roles:
                await inter.send('у вас уже это есть', ephemeral=True)
                return
            user = inter.user
            with open('/FluffBot/modules/currency/currency.json', 'r') as f:
                currency = json.load(f)

            if str(user.id) in currency:
                current_balance = currency[str(user.id)]
                if current_balance < 1000:
                    await inter.send('кажется что у тебя нехватает баланса для этой покупки :(', ephemeral=True)
                    return
                elif current_balance > 1000:
                    currency_remove(user=user, amount=1000)
                    await user.add_roles(role)
                    await inter.send(
                        'отлично! ты купил эту роль',
                        ephemeral=True)

                    print(f'{config.consE}{inter.user} купил роль фури гей')

        elif inter.component.custom_id == 'ShopFem':
            role = disnake.utils.get(inter.user.guild.roles, id=1251535800345034785)
            if role in inter.user.roles:
                await inter.send('у вас уже это есть', ephemeral=True)
                return
            user = inter.user
            with open('/FluffBot/modules/currency/currency.json', 'r') as f:
                currency = json.load(f)

            if str(user.id) in currency:
                current_balance = currency[str(user.id)]
                if current_balance < 1000:
                    await inter.send('кажется что у тебя нехватает баланса для этой покупки :(', ephemeral=True)
                    return
                elif current_balance > 1000:
                    currency_remove(user=user, amount=1000)
                    await user.add_roles(role)
                    await inter.send(
                        'отлично! ты купил эту роль',
                        ephemeral=True)

                    print(f'{config.consE}{inter.user} купил роль фембой')

        elif inter.component.custom_id == 'ShopPedcarlik':
            role = disnake.utils.get(inter.user.guild.roles, id=1254867795452366959)
            if role in inter.user.roles:
                await inter.send('у вас уже это есть', ephemeral=True)
                return
            user = inter.user
            with open('/FluffBot/modules/currency/currency.json', 'r') as f:
                currency = json.load(f)

            if str(user.id) in currency:
                current_balance = currency[str(user.id)]
                if current_balance < 1000:
                    await inter.send('кажется что у тебя нехватает баланса для этой покупки :(', ephemeral=True)
                    return
                elif current_balance > 1000:
                    currency_remove(user=user, amount=1000)
                    await user.add_roles(role)
                    await inter.send(
                        'отлично! ты купил эту роль',
                        ephemeral=True)

                    print(f'{config.consE}{inter.user} купил роль карлик педофилй')

        elif inter.component.custom_id == 'ShopEsh':
            role = disnake.utils.get(inter.user.guild.roles, id=1255129169306718361)
            if role in inter.user.roles:
                await inter.send('у вас уже это есть', ephemeral=True)
                return
            user = inter.user
            with open('/FluffBot/modules/currency/currency.json', 'r') as f:
                currency = json.load(f)

            if str(user.id) in currency:
                current_balance = currency[str(user.id)]
                if current_balance < 1000:
                    await inter.send('кажется что у тебя нехватает баланса для этой покупки :(', ephemeral=True)
                    return
                elif current_balance > 1000:
                    currency_remove(user=user, amount=1000)
                    await user.add_roles(role)
                    await inter.send(
                        'отлично! ты купил эту роль',
                        ephemeral=True)

                    print(f'{config.consE}{inter.user} купил роль карлик педофилй')


def setup(client):
    client.add_cog(SvShop(client))
