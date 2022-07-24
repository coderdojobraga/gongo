import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command(name="help")
    async def help(self, ctx: discord.ext.commands.Context) -> None:

        # Embed sent by the bot
        embed = discord.Embed(
            title="Comandos: [Obrigatório] <Opcional> (alias)", color=0x3489EB
        )

        fields = [
            ("$help", "É preciso apresentações?"),
            ("$promove [ninja] [cinturão]", "Promove um ninja para o cinturão dado."),
        ]

        for name, value in fields:
            embed.add_field(name=name, value=value, inline=False)

        await ctx.reply(embed=embed)


def setup(client):
    client.add_cog(Help(client))
