from discord.ext import commands
from discord import app_commands, Interaction

class TestCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="test")
    async def test(self, interaction: Interaction):
        print("\nrun")
        await interaction.response.send_message("Successfully sent", ephemeral=True)

async def setup(bot):
    await bot.add_cog(TestCog(bot))
