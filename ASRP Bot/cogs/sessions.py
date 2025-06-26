import discord
from discord.ext import commands
from discord import app_commands, Interaction
from utils.colors import get_session_color
from utils.session_views import SessionsMenu


class SessionCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="server-status", description="Change the server status!")
    async def session_manager(self, interaction: Interaction):
        from config import session_status, GREEN_SESSION_IMG, RED_SESSION_IMG

        if session_status == "ssu":
            img = GREEN_SESSION_IMG
            emoji = "<:ServerSSU:1316165992727973948>"
        elif session_status == "ssd":
            img = RED_SESSION_IMG
            emoji = "<:ServerSSD:1316165994124804116>"

        embed = discord.Embed(
            title="Session Manager Embed",
            description=f"\n### __{emoji} | Current Status: {session_status.upper()}__\n\n",
            color=discord.Color.from_str(get_session_color(session_status))
        )

        embed.set_image(url=img)

        embed.add_field(name="__<:ServerSSU:1316165992727973948> | Session Start Up__", value="> Start a session", inline=True)
        embed.add_field(name="__<:ServerSSD:1316165994124804116> | Session Shut Down__", value="> End an active session", inline=True)
        embed.add_field(name="__<:ServerLLP:1316165989012082708> | Low Player Ping__", value="> Send the low player ping", inline=True)
        embed.add_field(name="__<:ServerRestart:1386846452805931021> | Server Restart__", value="> Send the server restart message", inline=True)
        embed.add_field(name="__<:ServerCrash:1316165991561957447> | Session Crash__", value="> Send the session crash message", inline=True)
        embed.add_field(name="__<:ServerUpdate:1316165989963927645> | PRC Update__", value="> Send the session update message", inline=True)

        view = SessionsMenu(self.bot, session_status)
        await interaction.response.send_message(embed=embed, ephemeral=True, view=view)


async def setup(bot):
    await bot.add_cog(SessionCog(bot))
