from disnake.ext.commands import Cog
import disnake
from FluffBot.modules.AvatarProces.DefAvatarColor import process_avatar
from FluffBot import config
from FluffBot.modules.FanModules.IQ.IQDef import iq
import json


class MemberJoin(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(config.MemberJoinChannel)  # Получаем канал приветствия

        # Получаем список приглашений на сервере до присоединения участника
        invites_before_join = await member.guild.invites()

        # Вызываем функцию для получения IQ пользователя
        iq(user=member)

        # Определяем цвет аватара пользователя
        if member.avatar is not None:
            color = process_avatar(member)
        else:
            color = 0x23272A

        # Читаем JSON счетчика IQ
        with open(config.iq, 'r') as f:
            iq_count = json.load(f)

        # Получаем текущий IQ пользователя
        iq_user = iq_count.get(str(member.id), 'не удалось вывести IQ...')

        # Получаем список приглашений на сервере после присоединения участника
        invites_after_join = await member.guild.invites()

        inviter_name = 'не удалось найти...'

        # Находим приглашение, которое было использовано для присоединения участника
        for invite_before in invites_before_join:
            for invite_after in invites_after_join:
                if invite_before.code == invite_after.code and invite_before.uses < invite_after.uses:
                    inviter_name = invite_after.inviter.name
                    break
            if inviter_name != 'не удалось найти...':  # Если нашли имя пригласившего, выходим из цикла
                break

        # Формируем Embed сообщение для приветствия
        embed = disnake.Embed(
            title=f'{member.name}, ты #{member.guild.member_count} участник',
            description=f'✅верификация - https://discord.com/channels/1152572002088009749/1188213227620925531 \n🚫правила - https://discord.com/channels/1152572002088009749/1181974685773217824 \nего пригласил `{inviter_name}`\nIQ : {iq_user}',
            colour=color
        )
        embed.set_thumbnail(url=member.avatar.url)

        # Отправляем сообщение приветствия
        await channel.send(f'Привет <@{member.id}>🎉', embed=embed)

        # Выводим оповещение в консоль
        print(f'{config.console_event} присоединился участник - {member.name}, пригласил {inviter_name}')

def setup(bot):
    bot.add_cog(MemberJoin(bot))
