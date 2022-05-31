import os

import logging

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

logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='bot/discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

@client.event
async def on_ready():
    '''Client event that run when the program is ready.'''

    logger.info("The bot was logged in")
    DailyReport(client).report.start()
    logger.info("The task has been loaded")

@client.command()
async def load(ctx, extension):
    '''
    Command to load an extension.
    
    Parameters:
    ctx (discord.ext.commands.Context): Represents the context in which a command is being invoked under.
    extension (bot.cogs.[extension]): Represents the functionality to be loaded.

    '''
    
    client.load_extension(f'bot.cogs.{extension}')
    await ctx.send(
        f'O cog {extension} foi ativado.'
    )

@client.command()
async def unload(ctx, extension):
    '''
    Command to unload an extension.
    
    Parameters:
    ctx (discord.ext.commands.Context): Represents the context in which a command is being invoked under.
    extension (bot.cogs.[extension]): Represents the functionality to be unloaded.

    '''
    client.unload_extension(f'bot.cogs.{extension}')

    await ctx.send(
        f'O cog {extension} foi desativado.'
    )


client.load_extension('bot.cogs.belts')
client.load_extension('bot.cogs.daily_report')
# for filename in os.listdir('bot/cogs'):
    # if filename.endswith('.py'):
    #     # client.load_extension(f'bot.cogs.{filename[:-3]}')

