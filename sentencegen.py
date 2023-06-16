import random
import discord
import json
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='!', help_command=None, intents=intents)

words_json = open("words.json", "r")
words = json.load(words_json)
words_json.close()
nouns = words['nouns']
verbs = words['verbs']
adjective = words['adjective']
adverb = words['adverb']
pronoun = words['pronoun']
sentence = words['sentence']


@bot.command()
async def sentincegen(ctx):
    lts = random.choice(sentence)
    lta = lts.split(' ')
    rsen = ""
    for x in lta:
        if int(x) == 1:
            rsen += random.choice(nouns)
            rsen += " "
        elif int(x) == 2:
            rsen += random.choice(verbs)
            rsen += " "
        elif int(x) == 3:
            rsen += random.choice(adjective)
            rsen += " "
        elif int(x) == 4:
            rsen += random.choice(adverb)
            rsen += " "
        elif int(x) == 5:
            rsen += random.choice(pronoun)
            rsen += " "
    await ctx.send(rsen)

# a list of words referenced
# https://eslgrammar.org/list-of-nouns/
# other list
# https://blog.prepscholar.com/verbs-list


async def setup(bot):
    # help page a found, I will credit if it can find it again
    # Every extension should have this function
    bot.add_command(sentincegen)
