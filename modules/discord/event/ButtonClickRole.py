import disnake
from disnake.ext import commands
from FluffBot import config


class Role(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_button_click(self, inter: disnake.MessageInteraction):
        if inter.component.custom_id not in ['apple_craft.online', 'hub.holly_world.ru']:
            return

        if inter.component.custom_id == 'apple_craft.online':  # если apple craft
            role_apple_craft = disnake.utils.get(inter.user.guild.roles, id=1206185401945952266)

            if role_apple_craft in inter.user.roles:
                await inter.response.send_message('вы отменили роль <@&1206185401945952266>', ephemeral=True)
                await inter.user.remove_roles(role_apple_craft)

                print(f'{config.console_event}{inter.user.name} отменил роль apple_craft')

            else:
                await inter.response.send_message('вы получили роль <@&1206185401945952266>', ephemeral=True)
                await inter.user.add_roles(role_apple_craft)

                print(f'{config.console_event}{inter.user.name} получил роль apple_craft')

        elif inter.component.custom_id == 'hub.holly_world.ru':  # если holly world
            role_holly_world = disnake.utils.get(inter.user.guild.roles, id=1191857989326475274)

            if role_holly_world in inter.user.roles:
                await inter.response.send_message('вы отменили роль <@&1191857989326475274>', ephemeral=True)
                await inter.user.remove_roles(role_holly_world)

                print(f'{config.console_event}{inter.user.name} отменил роль holly_world')

            else:
                await inter.response.send_message('вы получили роль <@&1191857989326475274>', ephemeral=True)
                await inter.user.add_roles(role_holly_world)

                print(f'{config.console_event}{inter.user.name} получил роль holly_world')


def setup(bot):
    bot.add_cog(Role(bot))
