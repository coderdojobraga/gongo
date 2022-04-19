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
        self.roles = [role for role in self.member.roles]

    def current_belt(self) -> tuple:
        highest_belt = Belts.Branco.name
        for role in self.roles:
            for belt in Belts:
                if belt.name == role:
                    highest_belt = belt.name
        
        return (
            highest_belt, 
            self.get_role_from_name(
                self.guild,
                highest_belt
            )
        )

    def next_belt(self):
        value = self.current_belt()[0].value + 1

        return self.get_role_from_name(
            self.guild,
            Belts(value).name
        )

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

        if belt == ninja.current_belt():
            await ctx.reply(
                f"Esse já é o teu cinturão do ninja {user}"
            )
        
        elif belt == ninja.next_belt():
            role = ninja.get_role_from_name(guild, belt)
            await member.add_roles(
                guild.get_role(role.id),
                reason = None,
                atomic = True
            )
        
        await ctx.send(
            f'{user} agora és cinturão {belt} :tada:'
        )

def setup(client):
    client.add_cog(BeltsAttributions(client))
