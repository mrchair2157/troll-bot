#Has the Trolling related functions
import random
import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='-', help_command=None)

@bot.command()
@commands.has_permissions(administrator=True)
async def trollspam(ctx,num,*,msg):
    x = 1
    if 500 < int(num):
        num = '500'
    while x <= int(num):
        await ctx.send(msg)
        print( x ,'/' , num , ',' , msg)
        time.sleep(0.75)
        x += 1

@bot.command()
async def ip(ctx,user):

    await ctx.channel.purge(limit=1)
    ip = (str(random.randint(0 , 255)) + '.' + str(random.randint(0 , 255)) + '.' + str(random.randint(0 , 255)) + '.' + str(random.randint(0 , 255)))
    await ctx.send(f'{user} your ip is {ip} your opinion is now null.')
    print(f'{user} your ip is {ip} your opinion is now null.')
    
@bot.command()
@commands.has_permissions(manage_messages=True)
async def trollclear(ctx, num=2):
    await ctx.channel.purge(limit=num)

@bot.command()
async def help(ctx):
    ip = (str(random.randint(0 , 255)) + '.' + str(random.randint(0 , 255)) + '.' + str(random.randint(0 , 255)) + '.' + str(random.randint(0 , 255)))
    await ctx.send(f'look familiar {ip}    :^).')
    await ctx.send('https://tenor.com/view/freddy-freddy-fazbear-freddy-fnaf-fnaf-fnaf-meme-gif-24466510')

def setup(bot):
    # Every extension should have this function
    bot.add_command(help)
    bot.add_command(ip)
    bot.add_command(trollclear)
    bot.add_command(trollspam)
