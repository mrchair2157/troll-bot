#GPL 3.0
import discord
from discord.ext import commands
import time
import random
import string

bot = commands.Bot(command_prefix='!', help_command=None)

ls = [ 
        "https://tenor.com/view/minecraft-boxer-boxing-minecraft-boxer-gif-18025297",
        "https://tenor.com/view/cry-about-it-gif-22026840",
        "https://tenor.com/view/cry-about-it-gif-22562868",
        "https://tenor.com/view/we-do-a-little-trolling-we-do-a-medium-amount-of-trolling-troll-trolling-peter-griffin-gif-20853348",
        "https://tenor.com/view/troll-trolling-little-trolling-large-trolling-mass-trolling-gif-20639425",
        "https://tenor.com/view/twitter-gif-21485745",
        "https://tenor.com/view/doom-eternal-we-do-a-little-trolling-meme-shitpost-gif-20934549",
        "https://tenor.com/view/cry-about-it-cry-about-it-gif-20003018",
        "https://tenor.com/view/among-us-cry-about-it-go-cry-about-it-sussy-sussy-imposter-gif-23140749",
        "https://tenor.com/view/cry-about-it-gigachad-average-fan-vs-average-enjoyer-average-fan-average-enjoyer-gif-22029021",
        "https://tenor.com/view/cry-about-it-gif-22562868",
        "https://tenor.com/view/lol-gif-22995330",
        "https://tenor.com/view/troll-pilled-gif-19289988",
        "https://tenor.com/view/cry-about-it-madness-combat-hank-mukbang-gif-21834144",
        "https://tenor.com/view/purple-man-dancing-pixels-gif-17422304",
        "https://tenor.com/view/troll-trolled-trollge-troll-success-gif-22597471",
        "https://tenor.com/view/funny-purchase-college-barack-obama-obama-barack-obama-gif-19072900", 
        "https://tenor.com/view/rat-make-out-rat-sniff-hey-do-you-want-to-make-out-do-you-want-to-make-out-gif-23560859",
        "https://tenor.com/view/turtle-animal-dance-cute-gif-8300057",
        "https://tenor.com/view/clash-royale-clash-royale-emote-gif-23858585", # 0 - 19?
]
iv = [
        "https://tenor.com/view/civ-civ6-get-on-civ-gif-22961237",
        "https://tenor.com/view/civ-civ5-civ-meme-civ5meme-humankind-gif-22585341",
        "https://tenor.com/view/civ5-civ4-civ1-civ6-look-at-these-yields-gif-24164271",
        "https://tenor.com/view/gandhi-india-ftw-victory-winning-gif-8758824",
        "https://tenor.com/view/civ-civilization-gilgamesh-gilgabro-fan-gif-21095212",
        ]
@bot.command()
async def pancake_mix(ctx):
    await ctx.send("https://www.amazon.com/Crocker-Bisquick-Complete-Pancake-Buttermilk/dp/B00DJQ2B2W/ref=zg_bs_16317311_22/144-2364321-1683057?pd_rd_i=B00DJQ2B2W&psc=1")

@bot.command()
async def troll(ctx):
    x = random.choice(ls)
    await ctx.send(x)


@bot.event
async def on_ready():
    print('trolling time')

@bot.command()
@commands.has_permissions(administrator=True)
async def trollspam(ctx,num,*,msg):
    x = 1
    while x <= int(num):
        await ctx.send(msg)
        print( x ,'/' , num , ',' , msg)
        time.sleep(0.75)
        x = x + 1



@bot.command()
async def civ(ctx):
    x = random.choice(iv)
    await ctx.send(x)

@bot.command()
async def ip(ctx,user):

    await ctx.channel.purge(limit=1)
    ip = (str(random.randint(0 , 999)) + '.' + str(random.randint(0 , 999)) + '.' + str(random.randint(0 , 999)) + '.' + str(random.randint(0 , 999)))
    await ctx.send(f'{user} your ip is {ip} your opinion is now null.')
    print(f'{user} your ip is {ip} your opinion is now null.')
    
@bot.command()
@commands.has_permissions(manage_messages=True)
async def trollclear(ctx, num=2):
    await ctx.channel.purge(limit=num)

@bot.command()
async def help(ctx):
    await ctx.send('There is no help. There is no hope.')

@bot.command()
async def swiss_roll(ctx):
    await ctx.send("https://www.amazon.com/Little-Debbie-Swiss-Rolls-Pack/dp/B086PG5NLC/ref=sr_1_2?dchild=1&keywords=swiss+rolls&qid=1587695174&sr=8-2%22")



bot.run('[Privite token here]')
