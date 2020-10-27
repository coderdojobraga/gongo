"""Gongo.

Usage:
  Gongo (promove | p) <user> a <belt>

"""
import discord
from docopt import docopt, DocoptExit

from bot import VERSION


class Gongo(discord.Client):
    async def on_ready(self):
        print(f'We have logged in as {self.user}!')

    async def on_message(self, message):
        if message.author.bot:
            return

        if not message.content.lower().startswith('gongo'):
            return

        if not "🛡️ Admin" in [role.name for role in message.author.roles]:
            await message.channel.send(
                "Não tens permissões para me usar. Tenta com sudo :clown:"
            )
            return

        try:
            arguments = docopt(__doc__,
                               argv=message.content.split()[1:],
                               help=False)

            if arguments['promove'] or arguments['p']:
                await message.channel.send(
                    f'<@{message.author.id}> quer promover {arguments["<user>"]} a cinturão {arguments["<belt>"]} :tada:'
                )

        except DocoptExit:
            await message.channel.send(
                f'Olá! Esse comando não é válido! Vê isto: ```{__doc__}```')
