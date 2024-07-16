import disnake
from disnake.ext import commands
from FluffBot import config
import random
from urllib.parse import urlparse


class LinkAutoMod(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.whitelist = config.LinkWhiteList

    @commands.Cog.listener()
    async def on_message(self, message: disnake.Message):
        if message.author == self.bot.user:
            return

        contains_unwhitelisted_link = await self.contains_unwhitelisted_link(message.content)

        if contains_unwhitelisted_link:
            await message.delete()

            text = random.choice(['Упс', 'Ой'])

            embed = disnake.Embed(
                title=f'{text}, кажется, что твоей ссылки нет в белом списке :(',
                description='',
                colour=0xeb459e,
            )
            embed.add_field(
                name='white list:',
                value='```' + '\n'.join([f'{url}' for url in self.whitelist]) + '```'
            )

            await message.channel.send(f'{message.author.mention}', embed=embed)

            print(f'{config.console_event}на {message.author.name} сработал LinkAutoMod : {message.content}')

    async def contains_unwhitelisted_link(self, content: str) -> bool:
        for word in content.split():
            if word.startswith(("http://", "https://")):
                parsed_url = urlparse(word)
                domain = f"{parsed_url.scheme}://{parsed_url.netloc}/"
                if all(domain != url for url in self.whitelist):
                    return True

        return False


def setup(bot: commands.Bot):
    bot.add_cog(LinkAutoMod(bot))
