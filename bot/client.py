import os

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

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    
    await ctx.send(
        f'O cog {extension} foi ativado.'
    )

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    
    await ctx.send(
        f'O cog {extension} foi desativado.'
    )

for filename in os.listdir('bot/cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'bot.cogs.{filename[:-3]}')

