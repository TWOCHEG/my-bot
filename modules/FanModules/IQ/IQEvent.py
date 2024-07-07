import disnake
import json
from disnake.ext import commands
from FluffBot import config
from FluffBot.modules.FanModules.IQ.IQDef import iq

intents = disnake.Intents.default()
intents.members = True

iq_ctx = [
    'IQ',
    'Iq',
    'iq',
    'iQ'
]


class IQEv(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        for iq_message in iq_ctx:
            if iq_message in message.content:
                if message.author.id == config.BotId:
                    return

                if message.reference:
                    original_message = await message.channel.fetch_message(message.reference.message_id)
                    iq(user=original_message.author)
                    with open(config.iq, 'r') as f:
                        iq_count = json.load(f)

                        if original_message.author.id == message.author.id:
                            if str(message.author.id) in iq_count:
                                iq_user = iq_count[str(message.author.id)]
                                await message.channel.send(f'твой IQ - {iq_user}', reference=message)
                        else:
                            if str(original_message.author.id) in iq_count:
                                iq_user = iq_count[str(original_message.author.id)]
                                await message.channel.send(f'IQ {original_message.author.name} - {iq_user}',
                                                           reference=message)

                else:
                    iq(user=message.author)
                    user = message.author
                    with open(config.iq, 'r') as f:
                        iq_count = json.load(f)

                    if str(user.id) in iq_count:
                        iq_user = iq_count[str(user.id)]
                        await message.channel.send(f'твой IQ - {iq_user}', reference=message)


def setup(client):
    client.add_cog(IQEv(client))
