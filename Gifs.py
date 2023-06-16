import discord
from discord.ext import commands
import random

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='-', help_command=None, intents=intents)


@bot.command()
async def troll(ctx):
    x = random.choice(ls)
    await ctx.send(x)


@bot.command()
async def purpleguy(ctx):
    x = random.choice(tmbts)
    await ctx.send(x)


@bot.command()
async def civ(ctx):
    x = random.choice(iv)
    await ctx.send(x)

# kinda useless


@bot.command()
async def pancake_mix(ctx):
    await ctx.send("https://www.amazon.com/Crocker-Bisquick-Complete-Pancake-Buttermilk/dp/B00DJQ2B2W/ref=zg_bs_16317311_22/144-2364321-1683057?pd_rd_i=B00DJQ2B2W&psc=1")
# also kinda useless


@bot.command()
async def swiss_roll(ctx):
    await ctx.send("https://www.amazon.com/Little-Debbie-Swiss-Rolls-Pack/dp/B086PG5NLC/ref=sr_1_2?dchild=1&keywords=swiss+rolls&qid=1587695174&sr=8-2%22")

ls = [  "https://tenor.com/view/we-do-a-little-trolling-we-do-a-medium-amount-of-trolling-troll-trolling-peter-griffin-gif-20853348",
        "https://tenor.com/view/doom-eternal-we-do-a-little-trolling-meme-shitpost-gif-20934549",
        "https://tenor.com/view/among-us-cry-about-it-go-cry-about-it-sussy-sussy-imposter-gif-23140749",
        "https://tenor.com/view/troll-pilled-gif-19289988",
        "https://tenor.com/view/troll-trolled-trollge-troll-success-gif-22597471",
        "https://tenor.com/view/funny-purchase-college-barack-obama-obama-barack-obama-gif-19072900", 
        "https://tenor.com/view/rat-make-out-rat-sniff-hey-do-you-want-to-make-out-do-you-want-to-make-out-gif-23560859",
        "https://tenor.com/view/touch-grass-touch-grass-gif-21734295",
        "https://c.tenor.com/kwJ4fEC7W4IAAAAM/pvz-plants.gif",
        "https://tenor.com/view/fail-lawn-mower-dragged-gif-7931983",
        "https://tenor.com/view/get-off-my-lawn-old-lady-sprinkler-grumpy-angry-gif-19033636",
        "https://tenor.com/view/pvz-plants-vs-zombies-plant-vs-zombie-plant-zombie-pea-gif-19750806",
        "https://media.discordapp.net/attachments/895418619666784286/928808807046451240/FE4A1361-C273-4597-BC48-D3431A35E002.gif",
        "https://tenor.com/view/troll-trollface-scary-void-scary-troll-face-gif-19777211",
        "https://www.youtube.com/watch?v=-imBnKqgKQs",
        "https://youtu.be/9eC_dmVemaw",
        "https://c.tenor.com/oSIiS53J_UMAAAAM/cat-dancing.gif",
]

    # 0 - 27???????? lol
iv = [
        "https://tenor.com/view/civ-civ6-get-on-civ-gif-22961237",
        "https://tenor.com/view/civ-civ5-civ-meme-civ5meme-humankind-gif-22585341",
        "https://tenor.com/view/civ5-civ4-civ1-civ6-look-at-these-yields-gif-24164271",
        "https://tenor.com/view/gandhi-india-ftw-victory-winning-gif-8758824",
        "https://tenor.com/view/civ-civilization-gilgamesh-gilgabro-fan-gif-21095212",
        ]
tmbts = [
        "https://tenor.com/view/purple-guy-purple-guy-fnaf-apollothealmighty-fnaf-fnaf-security-breach-gif-2485131",
        "https://tenor.com/view/purple-guy-murder-roblox-man-behind-slaughter-mm2-gif-17490514",
        "https://tenor.com/view/purple-man-dancing-pixels-gif-17422304",
        "https://tenor.com/view/purple-guy-gif-18501497",
    ]


async def setup(bot):
    # Every extension should have this function
    bot.add_command(troll)
    bot.add_command(purpleguy)
    bot.add_command(civ)
    bot.add_command(pancake_mix)
    bot.add_command(swiss_roll)
