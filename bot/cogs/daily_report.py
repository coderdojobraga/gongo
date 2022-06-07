import json
import time
from datetime import datetime

import discord
from discord.ext import commands, tasks
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from bot.cogs.belts import get_role_from_name
from bot.cogs.logs import AttributionLogs, Base, log_attribution
from bot.settings import GONGO_CHANNEL_ID

# SQLAlchemy setup
engine = create_engine("sqlite:///daily_logs.db")
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class DailyReport(commands.Cog):
    """
    This cog is responsible for the daily report.

    Attributes:
        filename (str): The name of the file that contains the daily report.
    """

    filename = "bot/cogs/logs.json"

    def __init__(self, client: commands.Bot):
        self.client = client

    @tasks.loop(hours=1)
    async def report(self) -> None:
        """This function runs every hour to check if a report is needed"""

        # Search of the attributions made in the last 24 hours in the logs.json file
        current_timestamp = int(time.time())
        previous_day_timestamp = current_timestamp - (24 * 60 * 60)
        query_log = (
            session.query(AttributionLogs)
            .filter(AttributionLogs.timestamp > previous_day_timestamp)
            .all()
        )

        # Message to be sent to the admins
        # The message is only sent in case of daily_log not being empty
        current_time = datetime.now()
        msg = ""
        if query_log != [] and current_time.hour == 19:

            for info in query_log:
                msg += f"**{info.mentor_id}** atribuiu a **{info.ninja_id}** o cinturão {info.belt_attributed} - {datetime.fromtimestamp(info.timestamp)}\n"

            embed = discord.Embed(
                title=":scroll: Histórico de atribuições", description=msg
            )

            gongo_channel = self.client.get_channel(int(GONGO_CHANNEL_ID))
            await gongo_channel.send(embed=embed)


def setup(client: commands.Bot) -> None:
    client.add_cog(DailyReport(client))
