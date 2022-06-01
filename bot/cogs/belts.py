from enum import Enum, unique
from datetime import date
import json

from bot.cogs.logs import log_attribution

import discord
from discord.ext import commands


class FileHandler():
    '''
    This is a class to handle a json file.

    Attributes:
        file (string): The path to the json file being handled.
    '''

    file = "bot/cogs/belts.json"

    def __init__(self: str, belt: str):
        '''
        The constructor for the FileHandler class.

        Parameters:
            color (int): Color code to be displayed in discord embed.
        '''
        self.belt = belt
        self.msg = self.get_info()[0]
        self.color = self.get_info()[1]

    def get_info(self) -> tuple:
        '''
        The function to get the info from the belts.json file.

        Returns:
            msg (string): Variable that contains the message of the respective belt.
            color (int): Color code to be displayed in discord embed.
        '''
        with open(self.file) as json_file:
            data = json.load(json_file)
            msg = f"Subiste para {self.belt} :clap:\n\nPróximos objetivos:"
            color = int(data[self.belt]["color"], 16)
            for param in data[self.belt]["goals"]:
                msg += '\n' + param

            return (
                msg,
                color
            )

translator_to_emoji = {"Branco" : ":white_circle:",
                       "Amarelo" : ":yellow_circle:",
                       "Azul" : ":blue_circle:",
                       "Verde" : ":green_circle:",
                       "Laranja" : ":orange_circle:",
                       "Vermelho" : ":red_circle:",
                       "Roxo" : ":purple_circle:",
                       "Preto" : ":black_circle:"}

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

def get_role_from_name(guild: discord.Guild, belt: str) -> discord.Role:
    ''' This function returns the role of the respective belt. '''

    for role in guild.roles:
        if role.name == belt:
            return role

class Ninja():
    ''' This is a class to get information about a specific ninja. '''

    def __init__(self, guild: discord.Guild, member: discord.Member):
        self.guild = guild
        self.member = member
        self.roles = [role for role in member.roles]

    def current_belt(self) -> Belts:
        ''' This function returns the current belt of the ninja. '''

        highest_belt = None
        for role in self.roles:
            for belt in Belts:
                if belt.name == role.name:
                    highest_belt = belt
        
        return highest_belt

    def next_belt(self) -> Belts:
        ''' This function returns the next belt of the ninja. '''

        value = self.current_belt().value + 1 if self.current_belt().value < 8 else 8

        return Belts(value)
        

class BeltsAttributions(commands.Cog):
    ''' This is a class to handle the attribution of belts. '''

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command(name = 'promove')
    @commands.has_any_role("🛡️ Admin", "🏆 Champion", "🧑‍🏫 Mentores")
    async def promove(self, ctx: discord.ext.commands.Context, user: str , belt: str) -> None:
        ''' This function promotes a user to the next belt. '''

        mentions = ctx.message.raw_mentions
        guild = ctx.guild
        member = guild.get_member(mentions[0])
        ninja = Ninja(guild, member)

        if belt == "Branco" and ninja.current_belt() == None:
            role = get_role_from_name(guild, belt)
            
            await member.add_roles(
                guild.get_role(role.id),
                reason = None,
                atomic = True
            )

            # Public message
            await ctx.send(
                f'{user} agora és cinturão {belt} :tada:'
            )
            
            # Private message
            file_handler = FileHandler(belt)
            emoji = translator_to_emoji[belt]
            user = member
            embed = discord.Embed(
                title = f"{emoji} Parabéns, subiste de cinturão :tada:", 
                description = file_handler.msg, 
                color = file_handler.color
            )
            
            await user.send(embed = embed)
            log_attribution(member, ctx.author,  belt)

        elif belt == ninja.current_belt().name:
            await ctx.reply(
                f"Esse já é o cinturão do ninja {user}!"
            )
        
        elif belt == ninja.next_belt().name:
            role = get_role_from_name(guild, belt)
            await member.add_roles(
                guild.get_role(role.id),
                reason = None,
                atomic = True
            )

            # Public message
            await ctx.send(
                f'{user} agora és cinturão {belt} :tada:'
            )

            # Private message 
            file_handler = FileHandler(belt)
            emoji = translator_to_emoji[belt]
            user = member
            embed = discord.Embed(
                title = f"{emoji} Parabéns, subiste de cinturão :tada:", 
                description = file_handler.msg,
                color = file_handler.color
            )

            await user.send(embed = embed)
            log_attribution(member, ctx.author, belt)

        elif belt != ninja.next_belt().name:
            await ctx.send(
                f'{user} esse cinturão não é valido de se ser atribuido.'
            )

def setup(client: commands.Bot) -> None:
    client.add_cog(BeltsAttributions(client))
