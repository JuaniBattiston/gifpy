from gifpy import Gifpy
from discord.ext import commands
import random

bot = commands.Bot(command_prefix="!")
gifpy = Gifpy(key, "en_US")  # Your tenor API key goes here


@bot.event
async def on_ready():
    print("Bot Online!")


@bot.command()
async def gif(ctx, query):
    gif = gifpy.search(q=query, limit=1)
    await ctx.send(gif.url)


@bot.command()
async def randomgif(ctx, query):
    random_gif = gifpy.random_gif(q=query, limit=1)[0]
    await ctx.send(random_gif.url)


bot.run(token)  # Your bot token goes here
