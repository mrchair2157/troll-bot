import discord
from discord.ext import commands
import asyncio
tok= ""
intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='-', help_command=None, intents=intents)


async def main():
    print("Main Function")
    await bot.load_extension("wiki")
    await bot.load_extension("Gifs")
    await bot.load_extension("Trolls")
    await bot.load_extension("sentencegen")
    await bot.start(tok)


@bot.event
async def on_ready():
    print('trolling time')


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
