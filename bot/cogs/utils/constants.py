from enum import Enum, unique

import discord
from discord.ext import commands

translator_to_emoji = {
    "Branco": ":white_circle:",
    "Amarelo": ":yellow_circle:",
    "Azul": ":blue_circle:",
    "Verde": ":green_circle:",
    "Laranja": ":orange_circle:",
    "Vermelho": ":red_circle:",
    "Roxo": ":purple_circle:",
    "Preto": ":black_circle:",
}

list_roles = [
    {"value": 1, "name": "Branco"},
    {"value": 2, "name": "Amarelo"},
    {"value": 3, "name": "Azul"},
    {"value": 4, "name": "Verde"},
    {"value": 5, "name": "Laranja"},
    {"value": 6, "name": "Vermelho"},
    {"value": 7, "name": "Roxo"},
    {"value": 8, "name": "Preto"},
    {"value": 9, "name": ":🙋 Voluntários"},
    {"value": 10, "name": "🧑‍🏫 Mentores"},
    {"value": 11, "name": "🛡️ Admin"},
    {"value": 12, "name": "🏆 Champion"},
]

VOLUNTARIO = list_roles[8]
MENTOR = list_roles[9]
ADMIN = list_roles[10]
CHAMPION = list_roles[11]


def get_role_from_name(guild: discord.Guild, belt: str) -> discord.Role:
    """This function returns the role of the respective belt."""

    for role in guild.roles:
        if role.name == belt:
            return role
