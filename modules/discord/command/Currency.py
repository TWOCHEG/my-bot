import random

from disnake.ext import commands
import json
from FluffBot import config


class CurrencyCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.cooldown(1, config.CommandCooldown, commands.BucketType.user)  # задержка на использование
    @commands.slash_command(description='покажет ваш текущий баланс')
    async def баланс(self, ctx):
        user = ctx.author
        with open(config.currency, 'r') as f:
            currency = json.load(f)

        if str(user.id) in currency:
            current_balance = currency[str(user.id)]

            if current_balance >= 0:
                tex = '😑'
            elif current_balance >= 200:
                tex = random.choice('уже неплохо :)', 'неплохо 🙂')
            elif current_balance >= 10000:
                tex = random.choice('у тебя уже очень много', 'вау, это уже много')
            elif current_balance >= 10000:
                tex = random.choice(
                    'у тебя уже больше 10к , даже не представляю как можно было убить столько времени на это...',
                    'как можно было убить столько времени на это')

            await ctx.send(f'ваш баланс: `{current_balance}`, {tex}', ephemeral=True)

        else:
            await ctx.send('кажется что у вас еще нету баланса, вы можете заработать баланс в `/кликер` или `/рулетка`',
                           ephemeral=True)

        print(f'{config.console_command}{ctx.author.name} использовал /баланс')


def setup(bot):
    bot.add_cog(CurrencyCommand(bot))
