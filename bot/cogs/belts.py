from enum import Enum, unique

import discord
from discord.ext import commands

@unique
class Belts(Enum):
    Branco = 1
    Amarelo = 2
    Azul = 3
    Verde = 4
    Laranja = 5
    Vermelho = 6
    Roxo = 7
    Preto = 8

class Ninja():
    def __init__(self, guild, member):
        self.guild = guild
        self.member = member
        self.roles = [role for role in member.roles]

    def current_belt(self):
        highest_belt = None
        for role in self.roles:
            for belt in Belts:
                if belt.name == role.name:
                    highest_belt = belt
        
        return highest_belt

    def next_belt(self):
        # Check if the maximum range has been exceeded 
        value = self.current_belt().value + 1 if self.current_belt().value < 8 else 8

        return Belts(value)
        
    @staticmethod
    def get_role_from_name(guild, belt):
        for role in guild.roles:
            if role.name == belt:
                return role
    
class BeltsAttributions(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name = 'promove')
    @commands.has_any_role("🛡️ Admin", "🏆 Champion", "🧑‍🏫 Mentores")
    async def promove(self, ctx, user, belt):

        mentions = ctx.message.raw_mentions
        guild = ctx.guild
        member = guild.get_member(mentions[0])
        ninja = Ninja(guild, member)

        if belt == "Branco" and ninja.current_belt() == None:
            role = Ninja.get_role_from_name(guild, belt)
            
            await member.add_roles(
                guild.get_role(role.id),
                reason = None,
                atomic = True
            )
        
            await ctx.send(
                f'{user} agora és cinturão {belt} :tada:'
            )
        
        elif belt == ninja.current_belt().name:
            await ctx.reply(
                f"Esse já é o cinturão do ninja {user}!"
            )
        
        elif belt == ninja.next_belt().name:
            role = Ninja.get_role_from_name(guild, belt)
            await member.add_roles(
                guild.get_role(role.id),
                reason = None,
                atomic = True
            )
        
            await ctx.send(
                f'{user} agora és cinturão {belt} :tada:'
            )
        
        elif belt != ninja.next_belt().name:
            await ctx.send(
                f'{user} esse cinturão não é valido de se ser atribuido.'
            )

def setup(client):
    client.add_cog(BeltsAttributions(client))
