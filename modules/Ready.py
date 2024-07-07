from disnake.ext import commands, tasks
from datetime import datetime
import disnake
from FluffBot import config


class BotReady(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{config.console_bot}Бот запущен')
        self.my_task.start()

    @tasks.loop(minutes=1)
    async def my_task(self):
        if self.bot.is_ready():
            now = datetime.now()
            current_time = now.strftime("%H:%M")
            await self.bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.watching, name=f'на время {current_time}...'))

    @commands.Cog.listener()
    async def on_disconnect(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f'{config.console_bot}Кажется что что-то пошло не так, бот отключился {current_time}')


def setup(bot):
    bot.add_cog(BotReady(bot))
