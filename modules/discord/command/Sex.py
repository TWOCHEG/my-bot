import disnake
from disnake.ext import commands

from FluffBot import config

import random

# оформление консоли
consC = '[/] | '
consS = '[S] | '


class SexCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.cooldown(1, config.CommandCooldown, commands.BucketType.user)  # задержка на использование
    @commands.slash_command(description='вы переспите с выбраным участником')  # команда /sex
    async def переспать(self, ctx, участник: disnake.Member):
        tex = random.randint(1, 5)
        if tex == 1:
            tex = 'пускай другие теперь живут с этим :)'
        elif tex == 2:
            tex = 'и что, что ей/ему всего 13 возвраст ведь неимеет значения?'
        elif tex == 3:
            tex = 'поздравляю вас'
        elif tex == 4:
            tex = 'надеюсь у вас все прошло отлично))))))'
        elif tex == 5:
            tex = 'думую у вас все хорошо 😃'

        if участник.id == config.BotId:
            await ctx.send("нет")
        elif участник.id == ctx.author.id:
            await ctx.send('выебать самого себя у тебя не получится прости :(')
        elif участник.id == config.GirlId:
            await ctx.send(
                f'<@{ctx.author.id}> переспал с {участник.mention}, и что, что ей всего 13 возвраст ведь неимеет значения?')
            gif = random.randint(1, 2)
            if gif == 1:
                await ctx.channel.send('https://media.tenor.com/j9FGUPo-9VUAAAAM/cum-cumshot.gif')
            elif gif == 2:
                await ctx.channel.send('https://media.tenor.com/r1sbLbqb_NoAAAAi/cum-funny.gif')
        else:
            await ctx.send(f'<@{ctx.author.id}> переспал с {участник.mention}, {tex}')
            gif = random.randint(1, 2)
            if gif == 1:
                await ctx.channel.send('https://media.tenor.com/j9FGUPo-9VUAAAAM/cum-cumshot.gif')
            elif gif == 2:
                await ctx.channel.send('https://media.tenor.com/r1sbLbqb_NoAAAAi/cum-funny.gif')

        print(f'{config.console_command}{ctx.author.name} использовал /sex')  # оповещение в консоль


def setup(bot: commands.Bot):
    bot.add_cog(SexCommand(bot))
