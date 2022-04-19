import discord
from discord.ext import commands
from enum import Enum, unique

from bot import VERSION

client = commands.Bot(command_prefix=commands.when_mentioned_or('$'),
                      help_command=None,
                      intents=discord.Intents.all(),
                      case_insensitive=True)


@unique
class Cinturoes(Enum):
    Branco = 1
    Amarelo = 2
    Azul = 3
    Verde = 4
    Laranja = 5
    Vermelho = 6
    Roxo = 7
    Preto = 8


class Ninja_data():
    def __init__(self, guild, member):
        self.guild = guild
        self.member = member

    def current_belt(self):
        for belt in self.member.roles:
            for cinturao in Cinturoes:
                if cinturao.name == belt.name:
                    return belt

    def next_belt(self):
        for belt in self.member.roles:
            for cinturao in Cinturoes:
                if cinturao.name == belt.name:
                    next_cinturao_value = cinturao.value + 1
                    return get_role_from_name(
                        self.guild,
                        Cinturoes(next_cinturao_value).name)


def get_role_from_name(guild, belt_name):
    for role in guild.roles:
        if role.name == belt_name:
            return role


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.command()
@commands.has_any_role("🛡️ Admin", "🏆 Champion", "🧑‍🏫 Mentores")
async def promove(ctx, user, belt):
    await ctx.send(f"<@{ctx.message.author.id}> quer promover {user} a {belt}")

    mentions = ctx.message.raw_mentions  #List of id mentions in the command
    guild = ctx.guild  #Guild of the command
    member = guild.get_member(
        mentions[0])  #gets the member of the mentioned id

    ninja = Ninja_data(guild, member)

    if belt == "Branco":
        
        cinturao = get_role_from_name(guild, "Branco").id
        await member.add_roles(guild.get_role(cinturao),
                               reason=None,
                               atomic=True)
        
        await ctx.send(f'{user} agora és cinturão {belt}')

    elif belt == ninja.current_belt().name:

        await ctx.send(
            f'<@{ctx.message.author.id}> esse já é o cinturão atual do ninja {user}'
        )

    elif ninja.next_belt().name == belt:

        await member.add_roles(guild.get_role(ninja.next_belt().id),
                               reason=None,
                               atomic=True)
        await member.remove_roles(guild.get_role(ninja.current_belt().id),
                                  reason=None,
                                  atomic=True)

        await ctx.send(f'{user} agora és cinturão {belt}')

    else:
        await ctx.send(
            f'<@{ctx.message.author.id}> esse cinturão não é valido de se ser atribuido'
        )
