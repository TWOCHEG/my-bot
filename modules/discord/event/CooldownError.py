from disnake.ext import commands


class CooldownError(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_slash_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(
                'ограничение на использование команды, попробуйте еще раз через %.2f секунд' % error.retry_after,
                ephemeral=True)
            raise error
