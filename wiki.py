import random
import discord
from discord.ext import commands


intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='-', help_command=None, intents=intents)


@bot.command()
async def search(ctx, *, url):
    url = url.replace(' ', '+')
    await ctx.send("https://en.wikipedia.org/w/index.php?go=Go&search="+url)


async def setup(bot):
    # Every extension should have this function
    bot.add_command(search)
