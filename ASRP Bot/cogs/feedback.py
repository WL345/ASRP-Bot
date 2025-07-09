import discord.ext.commands, config

class FeedbackCog(discord.ext.commands.Cog):
    def __init__(self, bot):
        self.bot: discord.ext.commands.Bot = bot

    @discord.app_commands.command(name="bot-feedback", description="Make a suggestion or report a bug within the bot!")
    @discord.app_commands.describe(feedback_type="What type of feedback are you giving?", feedback="What is the feedback?")
    @discord.app_commands.choices(
        feedback_type=
        [
            discord.app_commands.Choice(name="Suggestion for the bot", value="Suggestion"),
            discord.app_commands.Choice(name="Bug Report for the bot", value="Bug Report"),
            discord.app_commands.Choice(name="Other", value="Other")
        ])
    async def get_user_id(self, interaction: discord.Interaction, feedback_type: str, feedback: str):
        print(f"\n{interaction.user.name} - <@{interaction.user.id}> - Used the feedback command")

        class MarkFeedbackComplete(discord.ui.View):
            def __init__(self, bot):
                super().__init__()
                self.bot: discord.ext.commands.Bot = bot

            @discord.ui.button(label="Mark Complete", style=discord.ButtonStyle.green, custom_id="feedback:complete")
            async def confirm_button(self, interaction: discord.Interaction, button: discord.ui.Button):
                if interaction.user.name != "wl345":
                    interaction.response.send_message(
                        "Are you WL? I didn't think so. So BACK OFF buckaroo")
                    return
                og_embed = interaction.message.embeds[0]
                og_description = og_embed.description

                new_embed = discord.Embed(
                    title=og_embed.title,
                    description=og_description + f"\n\n> - **Completed** {config.current_time()}",
                    color=discord.Color.from_str(config.colors.LIGHT_GREEN)
                )
                new_embed.set_image(url=config.imgs.LIGHT_GREEN_IMG)
                await interaction.message.edit(embed=new_embed, view=None, content=None)

            @discord.ui.button(label="Deny", style=discord.ButtonStyle.red, custom_id="feedback:deny")
            async def deny_button(self, interaction: discord.Interaction, button: discord.ui.Button):
                if interaction.user.name != "wl345":
                    interaction.response.send_message(
                        "Are you WL? I didn't think so. So BACK OFF buckaroo")
                    return
                try:
                    class DenyModal(discord.ui.Modal, title="Reasoning"):
                        def __init__(self, bot, interaction):
                            super().__init__()
                            self.bot: discord.ext.commands.Bot = bot
                            self.interaction = interaction

                            self.reason = discord.ui.TextInput(label="reason", style=discord.TextStyle.long)

                            self.add_item(self.reason)

                        async def on_submit(self, interaction: discord.Interaction):
                            await interaction.response.defer()
                            reason = self.reason.value

                            og_embed = interaction.message.embeds[0]
                            og_description = og_embed.description

                            new_embed = discord.Embed(
                                title=og_embed.title,
                                description=og_description + f"\n\n> - **Denied** {config.current_time()}\n> - **Reason:** {reason}",
                                color=discord.Color.from_str(config.colors.RED)
                            )
                            new_embed.set_image(url=config.imgs.RED_SESSION_IMG)

                            await interaction.message.edit(embed=new_embed, view=None, content=None)

                    await interaction.response.send_modal(DenyModal(self.bot, interaction))
                except Exception as e:
                    print(e)

        embed = discord.Embed(
            title="New ASRP Bot Feedback!",
            description=f"""
> - **User Information:**
>    - **Suggested By:** {interaction.user.mention} (`{interaction.user.id}`)
>    - **Suggested** {config.current_time()}

> - **Feedback Information:**
>    - **Feedback Type:** `{feedback_type}`
>    - **Feedback:** ```{feedback}```
""",
            color=discord.Color.from_str(config.colors.LIGHT_BLUE)
        )

        embed.set_image(url=config.imgs.LIGHT_BLUE_IMG)

        view = MarkFeedbackComplete(self.bot)
        await self.bot.get_channel(config.channels.FEEDBACK).send(content="<@995686080030445578>", embed=embed, view=view)
        await interaction.response.send_message("Your feedback has been sent successfully. Thank you!", ephemeral=True)

async def setup(bot):
    await bot.add_cog(FeedbackCog(bot))
