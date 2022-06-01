import discord
from discord.ext import commands, tasks

import json

import time
from datetime import datetime

from bot.settings import GUILD_ID
from bot.cogs.belts import get_role_from_name


# Function to determin if a belt attribution was made under 24 hours
def is_under_24(attribution_timestamp: int, current_timestamp: int) -> bool:
    ''' This function determines if an attribution was made under 24 hours '''

    one_day_seconds = 24 * 60 * 60
    return int(current_timestamp) - int(attribution_timestamp) <= one_day_seconds


class DailyReport(commands.Cog):
    ''' 
    This cog is responsible for the daily report. 
    
    Attributes:
        filename (str): The name of the file that contains the daily report.
    '''

    filename = "bot/cogs/logs.json"

    def __init__(self, client: commands.Bot):
        self.client = client


    @tasks.loop(seconds=10.0)
    async def report(self):
        ''' This function runs every 60 minutes to check if a report is needed '''

        daily_logs = []

        guild = self.client.get_guild(GUILD_ID)                     # guild the bot is operating in 
        admin_role = get_role_from_name(guild, "🛡️ Admin")          # guild  Admin role
        admin_members = admin_role.members                          # list of admins in the server

        with open(self.filename, "r") as json_file:
            logs_list = json.load(json_file)


        # Search of the attributions made in the last 24 hours in the logs.json file
        for attribution in reversed(logs_list):
            current_timestamp = int(time.time())
            if is_under_24(attribution["timestamp"], current_timestamp):
                daily_logs.append(attribution)
            else:
                break

        # Message to be sent to the admins
        # The message is only sent in case of daily_log not being empty
        msg = ""
        if daily_logs != []:

            for info in daily_logs:
                msg += f'**{info["mentor_id"]}** atribuiu a **{info["ninja_id"]}** o cinturão {info["belt_attributed"]} - {datetime.fromtimestamp(int(info["timestamp"]))}\n'

            embed = discord.Embed(
                title = ":scroll: Histórico de atribuições",
                description = msg
            )
            for member in admin_members:
                await member.send(embed=embed)


def setup(client: commands.Bot) -> None:
    client.add_cog(DailyReport(client))
