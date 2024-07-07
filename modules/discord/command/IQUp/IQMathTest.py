import disnake
from disnake.ext import commands
import random


def randomnum():
    a = random.randint(1, 100)
    return a


class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description='математический тест для повышения iq')
    async def iq(self, ctx):
        question1 = random.randint(1, 1)
        if question1 == 1:
            a = randomnum()
            b = randomnum()
            oper = random.randint(1, 3)
            if oper == 1:
                answer = a + b
                tex = f'{a} + {b} = ?'
            elif oper == 2:
                answer = a - b
                tex = f'{a} - {b} = ?'
            elif oper == 3:
                answer = a - b
                tex = f'{a} * {b} = ?'

            await ctx.send('начнем тест', ephemeral=True)
            embed1 = disnake.Embed(
                title='первый вопрос',
                description=f'{tex}'
            )

            await ctx.send(embed=embed1, components=[
                disnake.ui.Button(label=answer, style=disnake.ButtonStyle.gray, custom_id='TrueAnswer'),
                disnake.ui.Button(label=answerfalse, style=disnake.ButtonStyle.gray, custom_id='FalseAnswer')],
                                              ephemeral=True)


def setup(bot):
    bot.add_cog(Test(bot))
