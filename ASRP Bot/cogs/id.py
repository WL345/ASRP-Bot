import discord.ext

class IDCog(discord.ext.commands.Cog):
    # @discord.app_commands.guilds(discord.Object(id=1182487341386969158))
    @discord.app_commands.command(name="id", description="Get the ID for a given user")
    @discord.app_commands.describe(user="The user you want the ID of")
    async def get_user_id(self, interaction: discord.Interaction, user: discord.User):
        await interaction.response.send_message(f"```{user.id}```", ephemeral=True)


async def setup(bot):
    await bot.add_cog(IDCog())
