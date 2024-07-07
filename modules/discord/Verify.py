import disnake
from disnake.ext import commands
import random
import asyncio
from FluffBot import config


class Verification(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_button_click(self, inter: disnake.MessageInteraction):
        RoleVerify = disnake.utils.get(inter.user.guild.roles, id=1152573566571790437)
        if inter.component.custom_id not in ['начать', 'True', 'False']:
            return

        if RoleVerify in inter.user.roles:
            await inter.response.send_message('вы уже верифицированы', ephemeral=True)
            return

        elif inter.component.custom_id == 'начать':
            tex = random.randint(1, 10)
            if tex == 1:
                img = 'https://cdn.discordapp.com/attachments/1253349916764409966/1254752272261447690/IMG_20240616_144013_197.jpg?ex=667aa29d&is=6679511d&hm=ed3f57f2441d917b99a67036321d65a1a4dc6b87d42c4726166434b04ee14d19&'
                button1 = 'ты че еблан?'  # True
                button2 = 'да'  # False
            elif tex == 2:
                img = 'https://cdn.discordapp.com/attachments/1253349916764409966/1254752250161664020/Screenshot_2024-06-15-21-46-39-365_com.zhiliaoapp.musically-edit.jpg?ex=667aa298&is=66795118&hm=49a0b513aba67127ed29f5c386cf78067763db2e317086ef044bebc07c3186e8&'
                button1 = 'словарь фуриеба'  # True
                button2 = 'блять че это нахуй'  # False
            elif tex == 3:
                img = 'https://cdn.discordapp.com/attachments/1253349916764409966/1254752352934694963/2211629-1663830092_54-damion-club-p-gachimuchi-akteri-instagram-60.png?ex=667aa2b1&is=66795131&hm=d993cef69e9bbe3fdf6975aac9f44c104b28d503b4c0a7d00562a7a2c91332c3&'
                button1 = 'легенда'  # True
                button2 = 'danger master⚤⚤⚤⚤⚤⚤'  # False
            elif tex == 4:
                img = 'https://cdn.discordapp.com/attachments/1253349916764409966/1254752292389785681/IMG_20240616_223250_842.jpg?ex=667aa2a2&is=66795122&hm=288263d0350c160c16c8f2c4be3d52ff081262a2ec8030fd499c16e750e249d5&'
                button1 = 'лего человечка'  # True
                button2 = 'осуждаю'  # False
            elif tex == 5:
                img = 'https://cdn.discordapp.com/attachments/1253349916764409966/1254752215852384318/w8So-dN5OT0.png?ex=667aa290&is=66795110&hm=42ae3be6c6866041cfd3850ec4270ed6b453362fe16f8b16c65027bfd7818c07&'
                button1 = 'скалу'  # True
                button2 = 'АХАХАХАХХАХАХАХХХХХХАХАХ'  # False
            elif tex == 6:
                img = 'https://cdn.discordapp.com/attachments/1253349916764409966/1254752599110979676/IMG_20240412_145227.jpg?ex=667aa2eb&is=6679516b&hm=07e13e8c9d2d5671eab7f2c8f3b45c04503c6ce4e30b43cd07ebe3202f3f26eb&'
                button1 = 'суслика'  # True
                button2 = 'не знаю'  # False
            elif tex == 7:
                img = 'https://cdn.discordapp.com/attachments/1253349916764409966/1254791848078213120/148301_to4uYjnczH_d1673eae_872c_4a56_8c52_6ac81af2.jpg?ex=667ac779&is=667975f9&hm=79b73700232476e074e8816c5c6b5c101b500ed68882cd2414f603575eb28033&'
                button1 = 'джокер ещкерееее'  # True
                button2 = 'динаху'  # False
            elif tex == 8:
                img = 'https://cdn.discordapp.com/attachments/1253349916764409966/1254792026298384404/s1600_maxresdefault.jpg?ex=667ac7a3&is=66797623&hm=ae9f7cf8a3b928a439f471e68e0622ca6121e1ec80649c48f881428d8b19e49f&'
                button1 = '1488'  # True
                button2 = 'иди нахуй'  # False
            elif tex == 9:
                img = 'https://cdn.discordapp.com/attachments/1253349916764409966/1254793415414124555/tpn-420362.jpg?ex=667ac8ef&is=6679776f&hm=e229adea40fb9d37789e114a2d36d894a87d388d95f2b389eb2a265b02f94391&'
                button1 = 'медни бычек ещкереее'  # True
                button2 = 'верификация хуйня'  # False
            elif tex == 10:
                img = 'https://cdn.discordapp.com/attachments/1253349916764409966/1254752435050909716/IMG_20240525_170153.jpg?ex=667b4b84&is=6679fa04&hm=9c167100fed3b336374c9fe0119b399a973312ef51fa31771b61689927e0a441&'
                button1 = 'HyperOS AOD(активный экран)'  # True
                button2 = 'ПАСХАЛКОВЫАЫВД'  # False

            embed = disnake.Embed(
                title='что вы здесь видите?',
                colour=0x212121,
            )
            embed.set_image(url=img)

            await inter.response.send_message('начнем верификацию (у тебя одна попытка) ', embed=embed, components=[
                disnake.ui.Button(label=button1, style=disnake.ButtonStyle.gray, custom_id='True'),
                disnake.ui.Button(label=button2, style=disnake.ButtonStyle.gray, custom_id='False')],
                                              ephemeral=True)

        elif inter.component.custom_id == 'True':
            embed = disnake.Embed(
                title='отлично, верификация пройдена',
                description='дополнительные роли можно получить на канале - https://discord.com/channels/1152572002088009749/1230880939618336840',
                colour=0x7FFF00,
            )
            await inter.user.add_roles(RoleVerify)
            await inter.response.send_message(embed=embed, ephemeral=True)

            print(f'{inter.user} прошел верификацию')

        elif inter.component.custom_id == 'False':
            await inter.response.send_message('неправильно!!!! `тебя кикнет через 5 сек`', ephemeral=True)

            await asyncio.sleep(5)
            await inter.user.kick(reason='не прошел верификацию')

            print(f'{inter.user} не прошел верификацию')


def setup(bot):
    bot.add_cog(Verification(bot))
