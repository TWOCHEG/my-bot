import disnake
from disnake.ext import commands
import json
import asyncio
from FluffBot import config


class CurrencyList(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.channel_id = config.CurrencyListChannel
        self.currency_file_path = config.CurrencyFile
        self.last_currency_state = {}

    async def update_currency(self):
        await asyncio.sleep(config.ListUpdatePreDelay)  # предв задержка
        while True:
            with open(self.currency_file_path, 'r') as f:
                currency = json.load(f)

            sorted_currency = {k: v for k, v in sorted(currency.items(), key=lambda item: item[1], reverse=True)}

            if sorted_currency != self.last_currency_state:
                self.last_currency_state = sorted_currency
                channel = self.bot.get_channel(self.channel_id)

                if channel:
                    message = 'Таблица балансов участников :\n'
                    guild = self.bot.get_guild(config.GuildId)

                    for idx, (user_id, balance) in enumerate(sorted_currency.items(), start=1):
                        member = guild.get_member(int(user_id))
                        if member:
                            if idx <= 3:
                                message += f'```{idx}. {member.name}: {balance}```\n'
                            else:
                                message += f'{idx}. {member.name}: {balance}\n'

                    embed = disnake.Embed(
                        title=f'{message}',
                        description='обновляется каждую минуту при изменении',
                        color=0xFFE4B5
                    )

                    history = await channel.history(limit=1).flatten()
                    for msg in history:
                        if msg.author == channel.guild.me:
                            await msg.delete()

                    await channel.send(embed=embed)

                    print(f'{config.console_bot}таблица баланса обновлена')

                await asyncio.sleep(config.ListUpdateDelay)

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.loop.create_task(self.update_currency())


def setup(bot):
    bot.add_cog(CurrencyList(bot))

