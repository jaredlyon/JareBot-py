import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

# set up logging
import logging
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

# set up intents
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# set up commands, set presence, and load the cogs
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    await client.change_presence(activity=discord.Game(name="with python3.9 for once"))
    bot.load_extension('cogs.roles')

# set up commands
@client.event
async def on_message(message):
    # don't respond to ourselves
    if message.author == client.user:
        return

# read the config file
with open('config.json') as f:
    config = json.load(f)

# run the bot using the token from the config file
client.run(config['token'], log_handler = handler)