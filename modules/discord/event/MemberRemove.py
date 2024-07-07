from disnake.ext.commands import Cog
from FluffBot import config


class MemberRemove(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(config.MemberRemoveChannel)
        await channel.send(f'{member.name} вышел')

        print(f'{config.console_event}{member.name} вышел')


def setup(bot):
    bot.add_cog(MemberRemove(bot))
