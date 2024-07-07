import disnake
from disnake.ext import commands
from FluffBot import config


class SendCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()  # /отправить
    @commands.cooldown(1, config.CommandCooldown, commands.BucketType.user)  # задержка на использование
    async def отправить(self, inter):
        pass

    @отправить.sub_command(description='бот отправит ваше встраивание')  # встраивание
    async def встраивание(self, ctx, текст: str, описание: str = '', текст2: str = '', описание2: str = ''):

        blacklist = [
            '<@',
            '@everyone',
            '@here',
            'https://'
        ]  # content black list

        embedlist = [
            текст,
            описание,
            текст2,
            описание2
        ]  # embed module list

        embed = disnake.Embed(
            title='в вашем встраивании есть запрещённый контекст',
            description='```упоминания \nупоминание everyone/here \nссылки```',
            colour=0xeb459e,
        )  # embed на случай black list

        for black in blacklist:
            for em in embedlist:
                if black in em:
                    await ctx.send(embed=embed, ephemeral=True)
                    return

        await ctx.send('встраивание отправлено', ephemeral=True)
        # embed
        embed = disnake.Embed(
            title=текст,
            description=описание,
            colour=0xFFFFFF,
        )
        embed.add_field(name=текст2, value=описание2)

        await ctx.channel.send(embed=embed)

        print(
            f'{config.consC}{ctx.author.name} использовал /embed : {текст}, {описание}, {текст2}, {описание2}')  # оповещение в консоль

    @отправить.sub_command(description='бот отправит ваше сообщение')  # сообщение
    async def сообщение(self, ctx, сообщение: str):

        blacklist = [
            '<@',
            '@everyone',
            '@here',
            'https://'
        ]  # content black list

        embed = disnake.Embed(
            title='в вашем сообщении есть запрещённый контекст',
            description='```упоминания \nупоминание everyone/here \nссылки```',
            colour=0xeb459e,
        )  # embed на случай black list

        for blackl in blacklist:
            if blackl in сообщение:
                await ctx.send(embed=embed, ephemeral=True)
                return

        await ctx.send('сообщение отправлено', ephemeral=True)
        # сообщение
        await ctx.channel.send(f'{сообщение}')

        print(f'{config.console_command}{ctx.author} использовал /сказать : {сообщение}')  # оповещение в консоль


def setup(bot):
    bot.add_cog(SendCommand(bot))
