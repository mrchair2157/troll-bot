#https://gist.github.com/deekayen/4148741
import random
import discord
import random
from discord.ext import commands
bot = commands.Bot(command_prefix='-', help_command=None)

words = open("1-1000.txt","r")
LOW = words.read()
LOW = LOW.split('\n')
words.close()
print("LOW has been read")

@bot.command()
async def sentincegen(ctx):
    WC = random.randint(5,17)
    sentince = ""
    for x in range(WC):
        sentince = sentince + ' ' + random.choice(LOW)
        x = x + 1

    sentince = sentince + "."
    print(sentince)
    await ctx.send(sentince)

        
def setup(bot):
    # Every extension should have this function
    bot.add_command(sentincegen)
