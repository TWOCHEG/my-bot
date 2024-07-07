from disnake.ext import commands
from datetime import timedelta
import disnake
from FluffBot import config


class AntiSpam(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.spam_count = {}

    async def SpamCheck(self, message):
        for god in config.GodList:  # участники на которых не будет работать антиспам
            if message.author.id == god:
                return

        # Проверка на повторяющиеся слова
        if len(message.content.split()) > config.CtxSpamCount:
            words = message.content.split()
            if any(words.count(word) > config.CtxSpamCount for word in words):
                await message.author.timeout(until=disnake.utils.utcnow() + timedelta(minutes=10))
                await message.channel.send(
                    'Вы использовали одни и те же слова слишком часто. Вы были отправлены в тайм-аут на 10 минут',
                    reference=message)

        # Проверка на упоминания
        if message.mentions and len(message.mentions) > config.MentionsSpamCount:
            await message.author.timeout(until=disnake.utils.utcnow() + timedelta(minutes=10))
            await message.channel.send(
                'Вы упомянули слишком много участников или отправили два сообщения с упоминанием подряд. Вы были отправлены в тайм-аут на 10 минут',
                reference=message
            )

        # проверка на повторяющийся сообщения
        if message.author.id not in self.spam_count:
            self.spam_count[message.author.id] = 1
        else:
            if message.content == self.bot.last_message:
                self.spam_count[message.author.id] += 1
                if self.spam_count[message.author.id] == config.MessageSpamCount:
                    await message.author.timeout(until=disnake.utils.utcnow() + timedelta(minutes=10))
                    await message.channel.send(f"{message.author.mention} Слишком много повторяющихся сообщений!", reference=message)
            else:
                self.spam_count[message.author.id] = 1

        self.bot.last_message = message.content

    @commands.Cog.listener()
    async def on_message(self, message):
        await self.SpamCheck(message)


def setup(bot):
    bot.add_cog(AntiSpam(bot))
