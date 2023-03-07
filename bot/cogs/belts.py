import asyncio
import time

import discord
from discord.ext import commands
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from bot.cogs.utils.constants import *
from bot.cogs.utils.file_handler import *
from bot.cogs.utils.logs import AttributionLogs, Base, log_attribution
from bot.cogs.utils.ninja import *
from bot.web import *

# sqlalchemy setup
engine = create_engine("sqlite:///bot/data/daily_logs.db")

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()


class BeltsAttributions(commands.Cog):
    """This is a class to handle the discord attribution of belt roles."""

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command(name="promove")
    @commands.has_any_role(Roles["ADMIN"].name, Roles["CHAMPION"].name)
    async def promove(
        self, ctx: discord.ext.commands.Context, user: str, belt: str
    ) -> None:
        """This function promotes a user to the next belt."""

        mentions = ctx.message.raw_mentions
        guild = ctx.guild
        member = guild.get_member(mentions[0])
        ninja = Ninja(guild, member)

        if belt == ninja.next_belt().name:
            role = get_role_from_name(guild, belt)

            # send request to update ninja belt
            ninja_username = member.name + "#" + member.discriminator
            status = await update_belt(ninja_username, belt)

            if status == 200:
                await member.add_roles(
                    guild.get_role(role.id), reason=None, atomic=True
                )

                # Public message
                asyncio.create_task(ctx.send(f"{user} agora és cinturão {belt} :tada:"))

                # Private message
                asyncio.create_task(self.send_private_message(member, belt))

                # Adding the log to the database
                asyncio.create_task(self.log(ctx, member, belt))
            else:
                await ctx.send(
                    f"Ocorreu um erro ao atualizar o cinturão do ninja {user} no site :(\nPor favor tente mais tarde."
                )

        elif belt == ninja.current_belt().name:
            await ctx.reply(f"Esse já é o cinturão do ninja {user}!")

        else:
            await ctx.send(f"{user} esse cinturão não é valido de se ser atribuido.")

    async def log(self, ctx, member, belt):
        """This function logs the belt attribution."""

        new_log = AttributionLogs(
            ninja_id=str(member),
            mentor_id=str(ctx.author),
            belt_attributed=belt,
            timestamp=int(time.time()),
        )

        session.add(new_log)
        session.commit()

    async def send_private_message(self, member, belt):
        """This function sends a private message to the member."""

        file_handler = FileHandler(belt)
        emoji = translator_to_emoji[belt]
        user = member
        embed = discord.Embed(
            title=f"{emoji} Parabéns, subiste de cinturão :tada:",
            description=file_handler.msg,
            color=file_handler.color,
        )

        await user.send(embed=embed)


def setup(client: commands.Bot) -> None:
    client.add_cog(BeltsAttributions(client))
