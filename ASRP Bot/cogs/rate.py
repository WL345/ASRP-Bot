import discord.ext, config

    ##################
### FIX STAFF CHECKING ###
    ##################

class RateCog(discord.ext.commands.Cog):
    def __init__(self, bot):
        self.bot: discord.ext.commands.Bot = bot

    @discord.app_commands.command(name="rate", description="Rate a staff member!")
    @discord.app_commands.describe(staff="Which staff member are you rating?", rating="How many stars would you give them?", reason="Why are you giving this rating?", agreement="You will be moderated if this is false, bias, etc.")
    @discord.app_commands.choices(
        rating=[
            discord.app_commands.Choice(name="⭐⭐⭐⭐⭐", value="⭐⭐⭐⭐⭐"),
            discord.app_commands.Choice(name="⭐⭐⭐⭐", value="⭐⭐⭐⭐"),
            discord.app_commands.Choice(name="⭐⭐⭐", value="⭐⭐⭐"),
            discord.app_commands.Choice(name="⭐⭐", value="⭐⭐"),
            discord.app_commands.Choice(name="⭐", value="⭐")
        ],
        agreement=[
            discord.app_commands.Choice(name="I understand, my rating is not false or bias.", value="<:Check:1209512754465996860>")
        ]
    )
    async def rate(self, interaction: discord.Interaction, staff: discord.Member, rating: str, reason: str, agreement: str):
        print(f"\n{interaction.user.name} - <@{interaction.user.id}> - Used the rate command")

        # if staff.get_role(1182827699132174407) is None:
        #     await interaction.response.send_message("This user is not a staff member!", ephemeral=True)
        #     return

        class ConfirmationButtons(discord.ui.View):
            @discord.ui.button(label="Good Rating", emoji="✔", style=discord.ButtonStyle.green)
            async def good(self, interaction: discord.Interaction, button: discord.ui.Button):
                try:
                    og_embed = interaction.message.embeds[0]
                    embed = discord.Embed(
                        title="Confirmed Rating!",
                        description=og_embed.description + f"\n\n> **Confirmed By: {interaction.user.mention}**\n> **Confirmed** {config.current_time()}",
                        color=discord.Color.from_str(config.colors.LIGHT_GREEN)
                    )
                    embed.set_footer(text=og_embed.footer.text, icon_url=og_embed.footer.icon_url)
                    embed.set_thumbnail(url=og_embed.thumbnail.url)
                    embed.set_image(url=config.imgs.LIGHT_GREEN_IMG)

                    await interaction.message.edit(content=None, embed=embed, view=None)
                except Exception as e:
                    print(e)

            @discord.ui.button(label="Troll/Bias", emoji="✖", style=discord.ButtonStyle.red)
            async def bad(self, interaction: discord.Interaction, button: discord.ui.Button):
                try:
                    og_embed = interaction.message.embeds[0]
                    embed = discord.Embed(
                        title="Denied Rating!",
                        description=og_embed.description + f"\n\n> **Denied By: {interaction.user.mention}**\n> **Denied** {config.current_time()}",
                        color=discord.Color.from_str(config.colors.RED)
                    )
                    embed.set_footer(text=og_embed.footer.text, icon_url=og_embed.footer.icon_url)
                    embed.set_thumbnail(url=og_embed.thumbnail.url)
                    embed.set_image(url=config.imgs.RED_SESSION_IMG)

                    await interaction.message.edit(content=None, embed=embed, view=None)
                except Exception as e:
                    print(e)

        embed = discord.Embed(
            title="Someone has rated a staff member!",
            description=f"""
> - **Rater:** {interaction.user.mention}
> - **Ratee:** {staff.mention}
> - **Stars Given:** {rating}
> - **Reasoning:** {reason}
> - **Rated** {config.current_time()}
> - **Agreement:** {agreement}""",
            color=discord.Color.from_str(config.colors.LIGHT_BLUE)
        )
        embed.set_image(url=config.imgs.LIGHT_BLUE_IMG)
        embed.set_footer(text="ASRP - Automated Rating Response System", icon_url=config.LOGO)
        embed.set_thumbnail(url=config.LOGO)

        view = ConfirmationButtons()
        await self.bot.get_channel(config.channels.RATING).send("<&1354933462892548257", embed=embed, view=view)
        await interaction.response.send_message(f"Successfully rated {staff.mention}. Thank you for your feedback!", ephemeral=True)



async def setup(bot):
    await bot.add_cog(RateCog(bot))
