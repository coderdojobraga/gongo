from enum import Enum, unique

import discord
from discord.ext import commands
from emoji import emojize

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

Roles = Enum(
    value="Roles",
    names=[
        (emojize(":older_man: Guardiões"), 1),
        ("GUARDIOES", 1),
        (emojize(":ninja: Ninja"), 2),
        ("NINJAS", 2),
        (emojize(":person_raising_hand: Voluntários"), 3),
        ("VOLUNTARIOS", 3),
        (emojize(":teacher: Mentores"), 4),
        ("MENTOR", 4),
        (emojize(":shield: Admin"), 5),
        ("ADMIN", 5),
        (emojize(":trophy: Champion"), 6),
        ("CHAMPION", 6),
    ],
)

Belts = Enum(
    value="Belts",
    names=[
        ("Branco", 1),
        ("Amarelo", 2),
        ("Azul", 3),
        ("Verde", 4),
        ("Laranja", 5),
        ("Vermelho", 6),
        ("Roxo", 7),
        ("Preto", 8),
    ],
)


def get_role_from_name(guild: discord.Guild, belt: str) -> discord.Role:
    """This function returns the role of the respective belt."""

    for role in guild.roles:
        if role.name == belt:
            return role
