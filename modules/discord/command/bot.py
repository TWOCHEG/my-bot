import disnake
from disnake.ext import commands
import psutil
from FluffBot import config


class botCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.cooldown(1, config.CommandCooldown, commands.BucketType.user)  # задержка на использование
    @commands.slash_command(description='информация о боте')
    async def bot(self, ctx):
        cpu = int(psutil.cpu_percent())
        if cpu >= 0:
            cpu = 'отличное'
            color = 0x98FB98
        elif cpu >= 30:
            cpu = 'хорошее'
            color = 0x00FF7F
        elif cpu >= 50:
            cpu = 'средние'
            color = 0xFF7F50
        elif cpu >= 70:
            cpu = 'плохое'
            color = 0xDC143C

        embed = disnake.Embed(
            title='информация о CPU бота',
            description=f'пинг - `{round(self.bot.latency * 1000)} мс` \nCPU - `{psutil.cpu_percent()}%` \nОЗУ - `{psutil.virtual_memory().available * 100 / psutil.virtual_memory().total}%` \nобщее состояние - `{cpu}` \nhttps://github.com/TWOCHEG/my-bot',
            color=color
        )

        await ctx.send(embed=embed)

        print(f'{config.console_command}{ctx.author} использовал /CPU')  # оповещение в консоль


def setup(bot: commands.Bot):
    bot.add_cog(botCommand(bot))
