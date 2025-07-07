import discord.ext.commands

class debugCog(discord.ext.commands.Cog):
    def __init__(self, bot):
        self.bot: discord.ext.commands.Bot = bot

    @discord.app_commands.command(name="debug", description="For Debugging purposes.")
    @discord.app_commands.describe(choice="pick an option")
    @discord.app_commands.choices(
        choice=[
            discord.app_commands.Choice(name="1", value="1"),
            discord.app_commands.Choice(name="2", value="2"),
            discord.app_commands.Choice(name="3", value="3")
        ]
    )
    async def debug(self, interaction: discord.Interaction, choice: str):
        print(f"\n{interaction.user.name} - <@{interaction.user.id}> - Used the debug command")
        if interaction.user.name != "wl345":
            await interaction.response.send_message("https://tenor.com/view/this-is-not-for-you-rudy-ayoub-this-aint-for-you-its-not-intended-for-you-gif-27340083", ephemeral=True)
            return

        pass

async def setup(bot):
    await bot.add_cog(debugCog(bot))
