from disnake.ext import commands
import random
from FluffBot import config


class juniper(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == config.JuniperId:
            if '<:naxyiidi:1208289040181231716>' in message.content:
                tex = random.randint(1, 4)
                if tex == 1:
                    tex = 'сам иди заебал'
                elif tex == 2:
                    tex = 'иди нахуй'
                elif tex == 3:
                    tex = '<:naxyiidi:1208289040181231716>'
                elif tex == 4:
                    tex = 'иди нахуй'
                await message.channel.send(f'{tex}', reference=message)

                print(f'{config.console_event}сработала зашита от джунипера')  # оповещение в консоль


def setup(client):
    client.add_cog(juniper(client))
