from tabnanny import check
from unicodedata import name
import discord
from discord.ext import commands
import traceback

from bot import VERSION

client = commands.Bot(
    command_prefix = commands.when_mentioned_or('$'),
    help_command = None,
    intents = discord.Intents.all(),
    case_insensitive = True
)

cinturoes = ["Branco", 
             "Amarelo", 
             "Laranja", 
             "Verde", 
             "Azul", 
             "Vermelho", 
             "Roxo", 
             "Preto"]

def get_role_from_name(guild, belt_name):
    for role in guild.roles:
        if role.name == belt_name:
            return role

class Ninja_data(): 

    def __init__(self, guild, member):
        self.guild = guild
        self.member = member 

    def current_belt(self):
        for belt in self.member.roles:
            for i in range(len(cinturoes)-1):
                if cinturoes[i] == belt.name:
                    return belt
    
    def next_belt(self):
        for belt in self.member.roles:
            for i in range(len(cinturoes)-1):
                if cinturoes[i] == belt.name:
                    return get_role_from_name(self.guild, cinturoes[i+1])
    

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.command()
@commands.has_any_role("🛡️ Admin", "🏆 Champion", "🧑‍🏫 Mentores")
async def promove(ctx, user, belt):
    await ctx.send(
        f"<@{ctx.message.author.id}> quer promover {user} a {belt}"
    ) 

    mentions = ctx.message.raw_mentions    #List of id mentions in the command
    guild = ctx.guild                      #Guild of the command
    member = guild.get_member(mentions[0]) #gets the member of the mentioned id           

    ninja = Ninja_data(guild, member)
    
    if belt == ninja.current_belt().name:
        await ctx.send(
            f'<@{ctx.message.author.id}> esse ja é o cinturão atual do ninja {user}'
            )
    elif ninja.next_belt().name == belt:  
        
        await member.add_roles(guild.get_role(ninja.next_belt().id), reason=None, atomic=True)
        await member.remove_roles(guild.get_role(ninja.current_belt().id), reason=None, atomic=True)
        
        await ctx.send(
            f'{user} agora és cinturão {belt}'
            )
    else: 
        await ctx.send(
            f'<@{ctx.message.author.id}> esse cinturão não é valido de se ser atribuido'
            )


@client.event
async def on_command_error(ctx, error: traceback.format_exc()):
    if isinstance(error, commands.UserInputError):
        embed = discord.Embed(
            title = 'ERRO',
            description = f'Olá! Esse comando não se usa assim! Vê isto: ...',
            color = discord.Color(0xcc7)
        )

