from disnake.ext import commands


class Metion(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        pass  # пока что в разработке


def setup(client):
    client.add_cog(Metion(client))
