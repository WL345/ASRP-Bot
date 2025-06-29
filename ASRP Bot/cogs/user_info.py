import discord.ext

class UserInfoCog(discord.ext.commands.Cog):
    @discord.app_commands.command(name="user-info", description="Get some information of a given Roblox user!")
    @discord.app_commands.describe(username="The Roblox user to get.")
    async def get_user_id(self, interaction: discord.Interaction, user: str):
        print(f"{interaction.user.name} - <@{interaction.user.id}> - Used the userinfo command")
        await interaction.response.send_message("Not a thing yet", ephemeral=True)


async def setup(bot):
    await bot.add_cog(UserInfoCog())
