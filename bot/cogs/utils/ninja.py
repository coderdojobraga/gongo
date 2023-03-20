import discord

from bot.cogs.utils.constants import *
from bot.cogs.utils.file_handler import *


class Ninja:
    """This is a class to get information about a specific ninja."""

    def __init__(self, guild: discord.Guild, member: discord.Member):
        self.guild = guild
        self.member = member
        self.roles = list(member.roles)

    def current_belt(self):
        """This function returns the current belt of the ninja."""

        highest_belt = None
        for role in self.roles:
            for belt in Belts:
                if belt.name == role.name:
                    highest_belt = belt

        return highest_belt

    def next_belt(self) -> Belts:
        """This function returns the next belt of the ninja."""

        if self.current_belt() == None:
            value = 1
        elif self.current_belt().value < 8:
            value = self.current_belt().value + 1

        else:
            value = 8

        return Belts(value)
