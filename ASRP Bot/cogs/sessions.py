import discord.ext.commands, config
from discord import app_commands, Interaction
from utils.session_views import SessionsMenu


class SessionCog(discord.ext.commands.Cog):
    def __init__(self, bot):
        self.bot: discord.ext.commands.Bot = bot

    @app_commands.command(name="server-status", description="Change the server status!")
    async def session_manager(self, interaction: Interaction):
        print(f"\n{interaction.user.name} - <@{interaction.user.id}> - Used the server-status command")
        from config import session_status

        if session_status == "ssu":
            img = config.imgs.GREEN_SESSION_IMG
            emoji = "<:ServerSSU:1316165992727973948>"
        elif session_status == "ssd":
            img = config.imgs.RED_SESSION_IMG
            emoji = "<:ServerSSD:1316165994124804116>"

        embed = discord.Embed(
            title=f"{emoji} | Alaska State Roleplay - Server Status Embed",
            description=f"> Below you will find a menu that will allow you to manage the in-game server status! Any abuse of this system will result in an immediate termination.\n> - **Current Server Status: {session_status.upper()} {emoji}**",
            color=discord.Color.from_str(config.get_session_color(session_status))
        )

        embed.set_image(url=img)
        embed.set_footer(text="Any abuse of this system will result in an immediate termination & possible ban.", icon_url=config.LOGO)
        embed.set_thumbnail(url=config.LOGO)

        embed.add_field(name="__<:ServerSSU:1316165992727973948> | Session Start Up__", value="> Send the Server Startup Message.\n> *Automatically deletes the SSD message!*", inline=True)
        embed.add_field(name="__<:ServerSSD:1316165994124804116> | Session Shut Down__", value="> Send the Server Shutdown Message.", inline=True)
        embed.add_field(name="__<:ServerLLP:1316165989012082708> | Low Player Ping__", value="> Send the Server Low Player Ping Message.\n> *Automatically deletes after 30 minutes!*", inline=True)
        embed.add_field(name="__<:ServerRestart:1386846452805931021> | Server Restart__", value="> Send the Server Restart Message.\n> *Automatically deletes after 30 minutes!*", inline=True)
        embed.add_field(name="__<:ServerCrash:1316165991561957447> | Session Crash__", value="> Send the Server Crash Message.\n> *Automatically deletes after 30 minutes!*", inline=True)
        embed.add_field(name="__<:ServerUpdate:1316165989963927645> | PRC Update__", value="> Send the PRC Update Message.\n> *Automatically deletes after 30 minutes!*", inline=True)

        view = SessionsMenu(self.bot, session_status)
        await interaction.response.send_message(embed=embed, ephemeral=True, view=view)


async def setup(bot):
    await bot.add_cog(SessionCog(bot))
