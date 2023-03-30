import discord
from discord.ext import commands
import json
import logging
import os

# sends all bot logs back to the console
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logging.getLogger().setLevel(logging.INFO)
logging.getLogger().addHandler(handler)

# sets up the bot
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='$', intents=intents)

# set up commands
# set presence to "with Python3.9"
# register all cogs
# logs loaded cogs to the console
@bot.event
async def on_ready():
    print(f'{bot.user} is connected to the following guilds:')
    for guild in bot.guilds:
        print(f'{guild.name}(id: {guild.id})')
    await bot.change_presence(activity=discord.Game(name='with Python3.9'))
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')
            print(f'Loaded {filename[:-3]}')

# logs the use of commands in the console
@bot.event
async def on_command(ctx):
    print(f'{ctx.author} used {ctx.command}')

# set up commands
@bot.event
async def on_message(message):
    # don't respond to ourselves
    if message.author == bot.user:
        return

# reloads all the cogs
@bot.command()
async def reload(ctx):
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.reload_extension(f'cogs.{filename[:-3]}')
            print(f'Reloaded {filename[:-3]}')
    await ctx.send('Reloaded all cogs')

# read the config file
with open('config.json') as f:
    config = json.load(f)

# then runs the bot using the token from the config file
bot.run(config['token'], log_handler = handler)