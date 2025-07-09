import discord.ext.commands, config


class DMCog(discord.ext.commands.Cog):
    def __init__(self, bot):
        self.bot: discord.ext.commands.Bot = bot

    @discord.app_commands.command(name="dm", description="DM a user of your choice, anonymously.")
    @discord.app_commands.describe(user="The user you want to DM.", message="The message you want to send.")
    async def get_user_id(self, interaction: discord.Interaction, user: discord.User, message: str):
        print(f"\n{interaction.user.name} - <@{interaction.user.id}> - Used the DM command")
        try:
            await user.send(message)
            await interaction.response.send_message(f":white_check_mark: Successfully DMed {user.mention}.", ephemeral=True)

            embed = discord.Embed(
                title="__Someone DMed Someone!__",
                description=f"""
> - **Used By:** {interaction.user.mention}
> - **DMed:** {user.mention}
> - **Time Used:** {config.current_time()}
> - **Message Content:** `{message}`
""",
                color=discord.Color.from_str(config.colors.LIGHT_BLUE)
            )

            embed.set_footer(text="ASRP - Automated Command Logging System", icon_url=config.LOGO)
            embed.set_image(url=config.imgs.LIGHT_BLUE_IMG)
            embed.set_thumbnail(url=config.LOGO)

            await self.bot.get_channel(config.channels.DM_LOGGING).send(embed=embed)

        except Exception as e:
            await interaction.response.send_message(f"I was unable to DM {user.mention}. This is the error I recieved - \n```{e}```")


async def setup(bot):
    await bot.add_cog(DMCog(bot))