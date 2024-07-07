import disnake
from disnake.ext import commands
from FluffBot import config
from FluffBot.modules.FanModules.currency.DefCurrency import currency_add


class ClickCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.cooldown(1, config.CommandCooldown, commands.BucketType.user)  # задержка на использование
    @commands.slash_command(description='типо ноткойна пон???')
    async def кликер(self, ctx):
        embed = disnake.Embed(
            title='кликай пупс, c каждым кликом + 1'
        )
        embed.set_image(url='https://cdn.discordapp.com/attachments/1253349916764409966/1257623933373513840/65cc5f0c5f64a019.PNG?ex=6685150f&is=6683c38f&hm=be0ff394cbd1e50a8d05ef58f366266e23c3ef82b6fefe590575800155162367&')

        await ctx.send(embed=embed, components=(
            disnake.ui.Button(label='кнопка', style=disnake.ButtonStyle.gray, custom_id='clicker')
        ))

        print(f'{config.console_command}{ctx.author.name} использовал /кликер')

    @commands.Cog.listener()
    async def on_button_click(self, inter: disnake.MessageInteraction):
        if inter.component.custom_id not in ['clicker']:
            return

        if inter.component.custom_id == 'clicker':
            currency_add(user=inter.user, amount=1)
            await inter.send('клик!', ephemeral=True)


def setup(bot: commands.Bot):
    bot.add_cog(ClickCommand(bot))
