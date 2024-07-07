from disnake.ext import commands
from FluffBot import config


class RicRoll(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if 'https://www.youtube.com/watch?v=dQw4w9WgXcQ' in message.content:
            await message.channel.send('хорошая попытка чел😈', reference=message)

            print(f'{config.console_event}на {message.author} сработал ответ на рикрол')  # оповещение в консоль


def setup(client):
    client.add_cog(RicRoll(client))
