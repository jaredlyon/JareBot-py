import discord
from discord.ext import commands
import json
import logging

with open("config.json") as json_data_file:
    config = json.load(json_data_file)

intents = discord.Intents.default()
intents.message_content = True
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

@bot.command()
async def collatz(ctx, arg):
    await ctx.send("> **The Collatz conjecture is a conjecture in mathematics that concerns sequences defined as follows: start with any positive integer *n*. "
                   + "Then each term is obtained from the previous term as follows: if the previous term is even, the next term is one half of the previous term. "
                   + "If the previous term is odd, the next term is 3 times the previous term plus 1. "
                   + "The conjecture is that no matter what value of *n*, the sequence will always reach 1.**\n-<https://en.wikipedia.org/wiki/Collatz_conjecture>")
    await ctx.send("Your number: " + arg)
    iterations = 0

    if arg.isdigit() and int(arg) > 1:
        sequence = []
        number = int(arg)
        sequence.append(number)

        while number != 1:
            if number % 2 == 0:
                number = number // 2
                sequence.append(number)
                iterations += 1
            else:
                number = (number * 3) + 1
                sequence.append(number)
                iterations += 1
        
        await ctx.send(f"Your number went through `{iterations}` iteration(s) before being reduced to `1`.")
        if len(sequence) <= 1000:
            await ctx.send(f"Final sequence: {sequence}.")
        else:
            await ctx.send("*Final sequence could not be displayed due to its length.*\nNice work finding a lengthy one, it's pretty hard to do this...")

    else:
        await ctx.send("Collatz only works with positive integers greater than 1! Usage: **$collatz <integer>**"
                       + "\nNegative numbers break this Collatz conjecture tester, since negative integers reveal three separate loops as "
                       + "opposed to the positive integer set's 4-2-1 loop.")

bot.run(config['token'], log_handler=handler, log_level=logging.DEBUG)