import disnake
from disnake.ext import commands

from FluffBot import config

import random

# оформление консоли
consC = '[/] | '
consS = '[S] | '


class ShootCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.cooldown(1, config.CommandCooldown, commands.BucketType.user)  # задержка на использование
    @commands.slash_command(description='расстреляете выбраного участника')  # команда /расстрелять
    async def расстрелять(self, ctx, участник: disnake.Member):
        tex = random.randint(1, 4)
        if tex == 1:
            tex = 'наверно он заслужил'
        elif tex == 2:
            tex = 'сигма 🥵'
        elif tex == 3:
            tex = 'жоска'
        elif tex == 4:
            tex = 'надеюсь он это заслужил'

        if участник.id == config.bot_id:
            await ctx.send('нет')
        elif участник.id == ctx.author.id:
            await ctx.send('растрелять самого себя не выход живи лучше дальше :)')
        else:
            await ctx.send(f'<@{ctx.author.id}> расстрелял с автомата {участник.mention}, {tex}')
            gif = random.randint(1, 5)
            if gif == 1:
                await ctx.channel.send('https://tenor.com/view/shooting-crazy-gun-gif-15109765')
            elif gif == 2:
                await ctx.channel.send('https://media.tenor.com/xZN0hnyem7QAAAAi/shoot-gun.gif')
            elif gif == 3:
                await ctx.channel.send('https://media1.tenor.com/m/j9iJSojRyb4AAAAC/stalin-shoot.gif')
            elif gif == 4:
                await ctx.channel.send('https://media1.tenor.com/m/n96t0fQk9-IAAAAC/gun-shooting.gif')
            elif gif == 5:
                await ctx.channel.send('https://media1.tenor.com/m/x8v1oNUOmg4AAAAd/rickroll-roll.gif')

        print(f'{config.console_command}{ctx.author.name} использовал /растрелять')  # оповещение в консоль


def setup(bot: commands.Bot):
    bot.add_cog(ShootCommand(bot))
