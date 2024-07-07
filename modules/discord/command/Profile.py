import disnake
from disnake.ext import commands
from FluffBot import config
from FluffBot.modules.AvatarProces.DefAvatarColor import process_avatar


class ProfileCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()  # /отправить
    async def просмотреть(self, inter):
        pass

    @commands.cooldown(1, config.CommandCooldown, commands.BucketType.user)  # задержка на использование
    @просмотреть.sub_command(description='выведет информацию о профиле')
    async def профиль(self, ctx, участник: disnake.Member):

        await ctx.send('начнем...')

        if участник.avatar is not None:
            colour = process_avatar(member=участник)
            avatar = 'нет'
        else:
            colour = 0x23272A
            avatar = 'да'

        tex = f'●︎ статус - {участник.raw_status} \n●︎ клиент - браузер : {участник.web_status}, пк/ноутбук : {участник.desktop_status}, телефон : {участник.mobile_status}'
        if участник.raw_status == 'offline':
            tex = f'●︎ статус - {участник.raw_status}'

        embed1 = disnake.Embed(
            title=f'информация о профиле ```{участник.name}``` \n`глобально`',
            description=f'● ник - {участник.name} \n{tex} \n● создан - {участник.created_at} \n● дискрименатор - {участник.discriminator} \n● айди - {участник.id} \n● тег - {участник.tag} \n● дефолт аватарка - {avatar}',
            colour=colour
        )
        embed1.set_image(url=участник.avatar)

        embed2 = disnake.Embed(
            title=f'`сервер`',
            description=f'● ник - {участник.nick} \n● присоединился - {участник.joined_at} \n● тайм аут - {участник.current_timeout}',
            colour=colour
        )
        embed2.set_image(url=участник.guild_avatar)

        await ctx.channel.send(embed=embed1)
        await ctx.channel.send(embed=embed2)

        print(f'{config.console_command}{ctx.author} использовал /профиль')


def setup(bot: commands.Bot):
    bot.add_cog(ProfileCommand(bot))
