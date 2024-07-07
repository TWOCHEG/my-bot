import disnake
from disnake.ext import commands
import config

from modules.Ready import BotReady
from FluffBot.modules.discord.event import (CooldownError, ButtonClickRole, MessageJuniper, BotMetion,
                                            MemberJoin, MemberRemove, MessageRicRoll)

from FluffBot.modules.discord.command import (Clicker, Roulette, Sex, CPU, Currency, Shoot, Send, Profile)
from FluffBot.modules.discord.command.IQUp.IQMathTest import Test

from FluffBot.modules.FanModules.currency.CurrencyList import CurrencyList
from FluffBot.modules.FanModules.currency.Shop import SvShop

from FluffBot.modules.discord.AutoMod import AntiSpam, Link

from FluffBot.modules.FanModules.IQ.IQEvent import IQEv
from FluffBot.modules.discord.Verify import Verification

# бот
FluffBot = commands.Bot(command_prefix=config.prefix, help_command=None, intents=disnake.Intents.all())

# on ready
FluffBot.add_cog(BotReady(FluffBot))
FluffBot.add_cog(CurrencyList(FluffBot))  # список балансов
FluffBot.add_cog(CooldownError.CooldownError(FluffBot))  # cooldown error

# cogs slash_command
FluffBot.add_cog(CPU.CpuCommand(FluffBot))  # / CPU
FluffBot.add_cog(Shoot.ShootCommand(FluffBot))  # / расстрелять
FluffBot.add_cog(Roulette.RouletteCommand(FluffBot))  # / рулетка
FluffBot.add_cog(Sex.SexCommand(FluffBot))  # / переспать
FluffBot.add_cog(Profile.ProfileCommand(FluffBot))  # / профиль
FluffBot.add_cog(Send.SendCommand(FluffBot))  # / отправить сообщение\встраивание
FluffBot.add_cog(Clicker.ClickCommand(FluffBot))  # / clicker
FluffBot.add_cog(Currency.CurrencyCommand(FluffBot))  # / баланс
FluffBot.add_cog(Test(FluffBot))  # / iq

# cog event
FluffBot.add_cog(Verification(FluffBot))  # верификация
FluffBot.add_cog(ButtonClickRole.Role(FluffBot))  # серверные роли
FluffBot.add_cog(MemberJoin.MemberJoin(FluffBot))  # приветствие
FluffBot.add_cog(MemberRemove.MemberRemove(FluffBot))  # прощание
FluffBot.add_cog(SvShop(FluffBot))  # магазин

# auto mod
FluffBot.add_cog(Link.LinkAutoMod(FluffBot))  # link AutoMod
FluffBot.add_cog(AntiSpam.AntiSpam(FluffBot))  # анти спам

# ответы на сообщения
FluffBot.add_cog(MessageRicRoll.RicRoll(FluffBot))  # ответ на рик рол
FluffBot.add_cog(MessageJuniper.juniper(FluffBot))  # ответ на сообщение JuniperBot
FluffBot.add_cog(BotMetion.Metion(FluffBot))  # упоминание бота (в разработке)
FluffBot.add_cog(IQEv(FluffBot))  # IQ

FluffBot.run(config.TOKEN)
