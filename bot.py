import discord
from discord.ext import commands
import time
import random
import string

bot = commands.Bot(command_prefix='-', help_command=None)

def main():
    
    bot.load_extension("sentencegen")
    bot.load_extension("Gifs")
    bot.run('token here')

@bot.event
async def on_ready():
    print('trolling time')


if __name__ == "__main__":
    main()
