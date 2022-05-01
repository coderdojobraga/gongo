import os
from bot.cogs.daily_report import DailyReport

import discord
from discord.ext import commands

from bot import VERSION

client = commands.Bot(
    command_prefix = commands.when_mentioned_or('$'),
    help_command = None,
    intents = discord.Intents.all(),
    case_insensitive = True
)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

    DailyReport(client, 18).report.start()
    print("The task has been loaded")

@client.command()
async def load(ctx, extension):
    client.load_extension(f'bot.cogs.{extension}')
    await ctx.send(
        f'O cog {extension} foi ativado.'
    )

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'bot.cogs.{extension}')

    await ctx.send(
        f'O cog {extension} foi desativado.'
    )


client.load_extension('bot.cogs.belts')
client.load_extension('bot.cogs.daily_report')
# for filename in os.listdir('bot/cogs'):
    # if filename.endswith('.py'):
    #     # client.load_extension(f'bot.cogs.{filename[:-3]}')

