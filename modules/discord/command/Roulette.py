import disnake
from disnake.ext import commands
import random
from datetime import timedelta
from FluffBot import config
from FluffBot.modules.FanModules.currency.DefCurrency import currency_add
from FluffBot.modules.FanModules.currency.DefCurrency import currency_remove
from FluffBot.modules.FanModules.IQ.IQDef import iq_add
from FluffBot.modules.FanModules.IQ.IQDef import iq_remove


class RouletteCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.cooldown(1, config.CommandCooldown, commands.BucketType.user)  # задержка на использование
    @commands.slash_command(description='тут вы можете попытать свою удачу')
    async def рулетка(self, ctx):

        await ctx.send('запускаю рандом....')
        await ctx.channel.send('https://media.tenor.com/AQQVuTU0ZjcAAAAi/casino.gif')
        await ctx.send('вы выиграли:')

        tex = random.randint(1, 24)  # генерируется приз
        # мега приз
        if tex == 1:
            await ctx.channel.send('`нихуя`')
        # роли
        if tex == 2:
            role = disnake.utils.get(ctx.author.guild.roles, id=1251535800345034785)
            if role in ctx.author.roles:
                await ctx.author.remove_roles(role)
                await ctx.channel.send('`изъятие роли фембоя`')
            else:
                await ctx.author.add_roles(role)
                await ctx.channel.send('`роль фембоя`')
        elif tex == 3:
            role = disnake.utils.get(ctx.author.guild.roles, id=1253710242466893894)
            if role in ctx.author.roles:
                await ctx.author.remove_roles(role)
                await ctx.channel.send('`изъятие роли педофила :(`')
            else:
                await ctx.author.add_roles(role)
                await ctx.channel.send('`роль педофила` 😈')
        elif tex == 4:
            role = disnake.utils.get(ctx.author.guild.roles, id=1253710242466893894)
            if role in ctx.author.roles:
                await ctx.author.remove_roles(role)
                await ctx.channel.send('`изъятие роли сигмы`')
                await ctx.channel.send('ты больше не сигма XD')
            else:
                await ctx.author.add_roles(role)
                await ctx.channel.send('`роль сигмы`')
        elif tex == 5:
            role = disnake.utils.get(ctx.author.guild.roles, id=1253434818125893784)
            if role in ctx.author.roles:
                await ctx.author.remove_roles(role)
                await ctx.channel.send('`изъятие роли фури гея`')
            else:
                await ctx.author.add_roles(role)
                await ctx.channel.send('`роль фури гея`')
        elif tex == 6:
            role = disnake.utils.get(ctx.author.guild.roles, id=1254867795452366959)
            if role in ctx.author.roles:
                await ctx.author.remove_roles(role)
                await ctx.channel.send('`изъятие роли карлика педофила`')
            else:
                await ctx.author.add_roles(role)
                await ctx.channel.send('`роль карлика педофила`')
        elif tex == 7:
            role = disnake.utils.get(ctx.author.guild.roles, id=1255129169306718361)
            if role in ctx.author.roles:
                await ctx.author.remove_roles(role)
                await ctx.channel.send('`изъятие роли ешкерийца`')
            else:
                await ctx.author.add_roles(role)
                await ctx.channel.send('`роль ешкерийца`')
        elif tex == 8:
            role = disnake.utils.get(ctx.author.guild.roles, id=1256547016742273065)
            if role in ctx.author.roles:
                await ctx.author.remove_roles(role)
                await ctx.channel.send('`изъятие роли потного толстого карлика`')
            else:
                await ctx.author.add_roles(role)
                await ctx.channel.send('`роль потного толстого карлика`')
        # муты
        elif tex == 9:
            await ctx.channel.send('`мут на час`')
            for god in config.GodList:
                if ctx.author.id == god:
                    await ctx.channel.send('кажется что вас невозможно замутить')
                    return
            await ctx.author.timeout(until=disnake.utils.utcnow() + timedelta(hours=1))
        elif tex == 10:
            await ctx.channel.send('`мут на 5 минут`')
            for god in config.GodList:
                if ctx.author.id == god:
                    await ctx.channel.send('кажется что вас невозможно замутить')
            await ctx.author.timeout(until=disnake.utils.utcnow() + timedelta(minutes=5))
        elif tex == 11:
            await ctx.channel.send('`мут на 10 минут`')
            for god in config.GodList:
                if ctx.author.id == god:
                    await ctx.channel.send('кажется что вас невозможно замутить')
            await ctx.author.timeout(until=disnake.utils.utcnow() + timedelta(minutes=10))
        elif tex == 12:
            await ctx.channel.send('`мут на 5 часов`')
            for god in config.GodList:
                if ctx.author.id == god:
                    await ctx.channel.send('кажется что вас невозможно замутить')
            await ctx.author.timeout(until=disnake.utils.utcnow() + timedelta(hours=5))
        # гифки
        elif tex == 13:
            gif1 = random.randint(1, 3)
            await ctx.channel.send('`гифку с t2x2`')
            if gif1 == 1:
                await ctx.channel.send('https://media1.tenor.com/m/JmOWGbpd7QMAAAAC/t2x2.gif')
            elif gif1 == 2:
                await ctx.channel.send('https://media1.tenor.com/m/46VmlJGf0UUAAAAC/не-зря-зря.gif')
            elif gif1 == 3:
                await ctx.channel.send('https://media1.tenor.com/m/UP5BKcQjumUAAAAd/t2x2-twerk.gif')
        elif tex == 14:
            gif2 = random.randint(1, 11)
            await ctx.channel.send('`гифку с фури`')
            if gif2 == 1:
                await ctx.channel.send('https://media1.tenor.com/m/SN105LAhhQAAAAAC/kromia-vr-chat.gif')
            elif gif2 == 2:
                await ctx.channel.send('https://media1.tenor.com/m/u3TBGrjhBiQAAAAC/dan.gif')
            elif gif2 == 3:
                await ctx.channel.send('https://media1.tenor.com/m/Mac7xklB0G4AAAAC/furry-smile.gif')
            elif gif2 == 4:
                await ctx.channel.send('https://media1.tenor.com/m/lxEADEENwQ0AAAAC/furry-interested.gif')
            elif gif2 == 5:
                await ctx.channel.send('https://media1.tenor.com/m/GlcNJ738bBcAAAAd/kromia-furrmia.gif')
            elif gif2 == 6:
                await ctx.channel.send('https://media1.tenor.com/m/4OKEy1q8GYQAAAAd/sonicfox-furry.gif')
            elif gif2 == 7:
                await ctx.channel.send('https://media1.tenor.com/m/OQM_n_HA0KYAAAAC/adastra-amicus.gif')
            elif gif2 == 8:
                await ctx.channel.send('https://media1.tenor.com/m/lD8v6U07EOoAAAAd/ankha-meme-animated.gif')
            elif gif2 == 9:
                await ctx.channel.send('https://media1.tenor.com/m/q2T3RB3hofsAAAAd/cheek-pull-furry.gif')
            elif gif2 == 10:
                await ctx.channel.send('https://media1.tenor.com/m/4JmqGlO0EB0AAAAC/icon-furry.gif')
            elif gif2 == 11:
                await ctx.channel.send('https://media1.tenor.com/m/XLrBBmmPDNMAAAAd/t2x2-скырлы.gif')
        elif tex == 15:
            await ctx.channel.send('`рикрол`')
            await ctx.channel.send('https://media1.tenor.com/m/x8v1oNUOmg4AAAAd/rickroll-roll.gif')
        elif tex == 16:
            gif3 = random.randint(1, 3)
            await ctx.channel.send('`гифку с сигмой`')
            if gif3 == 1:
                await ctx.channel.send('https://tenor.com/view/patrick-bateman-sigma-yes-gif-26992928')
            elif gif3 == 2:
                await ctx.channel.send('https://media1.tenor.com/m/n8Qkkhyq7WkAAAAd/сигма-сигма-мем.gif')
            elif gif3 == 3:
                await ctx.channel.send('https://media1.tenor.com/m/58JYPZHgrg0AAAAd/sigma-patrick-bateman.gif')
        elif tex == 17:
            gif4 = random.randint(1, 3)
            await ctx.channel.send('`гифку с мьюингом`')
            if gif4 == 1:
                await ctx.channel.send('https://media1.tenor.com/m/YNvTXqUU1isAAAAC/mewing-cat-mewing.gif')
            elif gif4 == 2:
                await ctx.channel.send('https://media1.tenor.com/m/rH9J08_cfjEAAAAd/giga-gigacat.gif')
            elif gif4 == 3:
                await ctx.channel.send('https://media1.tenor.com/m/zAC9qD2eNPAAAAAd/mewing.gif')
        elif tex == 18:
            gif5 = random.randint(1, 5)
            await ctx.channel.send('`гифку про пасхалку`')
            if gif5 == 1:
                await ctx.channel.send('https://media1.tenor.com/m/OnFWLmSIhIAAAAAd/1488-джокер-пасхалко-мем2024.gif')
            elif gif5 == 2:
                await ctx.channel.send('https://media1.tenor.com/m/E_IxCQ6HSrgAAAAd/посхалко-1488-посхалко.gif')
            elif gif5 == 3:
                await ctx.channel.send('https://media.tenor.com/7-endVMZbCoAAAAi/eshkere-edgar.gif')
            elif gif5 == 4:
                await ctx.channel.send('https://media1.tenor.com/m/9cTQHFXC1ToAAAAd/пасхалка-посхалко.gif')
            elif gif5 == 5:
                await ctx.channel.send('https://media1.tenor.com/m/zBKTbT49iY0AAAAC/ppp.gif')
        # баланс
        elif tex == 19:
            currency_add(user=ctx.author, amount=500)
            await ctx.channel.send('`10 Койнов`')
        elif tex == 20:
            currency_add(user=ctx.author, amount=1001)
            await ctx.channel.send('`100 Койнов`')
        elif tex == 21:
            currency_remove(user=ctx.author, amount=500)
            await ctx.channel.send('`-50 Койнов`')
        elif tex == 22:
            coin = random.randint(1, 100)
            currency_add(user=ctx.author, amount=coin)
            await ctx.channel.send(f'`{coin} Койнов`')
        elif tex == 23:
            iq_add(user=ctx.author, amount=10)
            await ctx.channel.send(f'`10 IQ`')
        elif tex == 24:
            iq_remove(user=ctx.author, amount=10)
            await ctx.channel.send(f'`-10 IQ`')

        print(f'{config.console_command}{ctx.author.name} использовал /рулетка')  # оповещение в консоль


def setup(bot: commands.Bot):
    bot.add_cog(RouletteCommand(bot))
