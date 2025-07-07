import discord.ext

class DepartmentsView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)  # Persistent view

    @discord.ui.button(label="More Info", style=discord.ButtonStyle.primary, custom_id="departments")
    async def departments_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Here is more info about the departments.", ephemeral=True)

class DepartmentsCog(discord.ext.commands.Cog):
    def __init__(self, bot):
        self.bot: discord.ext.commands.Bot = bot

    @discord.app_commands.command(name="departments", description="Update the Departments Embed")
    async def get_user_id(self, interaction: discord.Interaction, user: discord.User):
        embed = discord.Embed(
            title="Departments",
            description="Stuff"
        )

        view = DepartmentsView()
        await interaction.response.send_message(embed=embed, view=view)



async def setup(bot):
    await bot.add_cog(DepartmentsCog(bot))
