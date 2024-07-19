# main file
import disnake
from disnake.ext import commands
import config

# cogs
from modules.Ready import BotReady
from FluffBot.modules.FanModules.currency.CurrencyList import CurrencyList
from FluffBot.modules.FanModules.currency.Shop import SvShop
from FluffBot.modules.discord.command.Clicker import ClickCommand
from FluffBot.modules.discord.AutoMod.AntiSpam import AntiSpam
from FluffBot.modules.FanModules.IQ.IQEvent import IQEv
from FluffBot.modules.discord.Verify import Verification
from FluffBot.modules.discord.command import Roulette, Sex, CPU, Currency, Shoot, Send, Profile
from FluffBot.modules.discord.event import CooldownError, ButtonClickRole, MessageJuniper, BotMetion, MemberJoin, \
    MemberRemove, MessageRicRoll
from FluffBot.modules.discord.AutoMod import Link

# bot
FluffBot = commands.Bot(command_prefix=config.prefix, help_command=None, intents=disnake.Intents.all())

cogs = [
    BotReady(FluffBot),
    CurrencyList(FluffBot),
    CooldownError.CooldownError(FluffBot),
    CPU.CpuCommand(FluffBot),
    Shoot.ShootCommand(FluffBot),
    Roulette.RouletteCommand(FluffBot),
    Sex.SexCommand(FluffBot),
    Profile.ProfileCommand(FluffBot),
    Send.SendCommand(FluffBot),
    ClickCommand(FluffBot),
    Currency.CurrencyCommand(FluffBot),
    Verification(FluffBot),
    ButtonClickRole.Role(FluffBot),
    MemberJoin.MemberJoin(FluffBot),
    MemberRemove.MemberRemove(FluffBot),
    SvShop(FluffBot),
    Link.LinkMessage(FluffBot),
    AntiSpam(FluffBot),
    MessageRicRoll.RicRoll(FluffBot),
    MessageJuniper.juniper(FluffBot),
    BotMetion.Metion(FluffBot),
    IQEv(FluffBot)
]

for cog in cogs:
    FluffBot.add_cog(cog)

FluffBot.run(config.TOKEN)
