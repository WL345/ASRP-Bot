from discord.ext import commands
from discord import app_commands, Interaction

class SayCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="say")
    @app_commands.describe(message="message")
    async def say(self, interaction: Interaction, message: str):
        await interaction.channel.send(content=message)
        await interaction.response.send_message("Successfully sent", ephemeral=True)

async def setup(bot):
    await bot.add_cog(SayCog(bot))
