import discord, datetime


class MarkFeedbackComplete(discord.ui.View):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @discord.ui.button(label="Mark Complete", style=discord.ButtonStyle.green)
    async def confirm_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.name != "wl345":
            interaction.response.send_message("Are you the bot dev now? Are you WL? I didn't think so. So BACK OFF buckaroo")
            return

        og_embed = interaction.message.embeds[0]
        og_description = og_embed.description

        new_embed = discord.Embed(
            title=og_embed.title,
            description=og_description + f"\n\n> - **Completed** <t:{int(datetime.datetime.now().timestamp())}:R>",
            color=og_embed.color
        )
        new_embed.set_image(url=og_embed.image.url)
        await interaction.message.edit(embed=new_embed, view=None, content=None)

    @discord.ui.button(label="Deny", style=discord.ButtonStyle.red)
    async def deny_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.name != "wl345":
            interaction.response.send_message("Are you the bot dev now? Are you WL? I didn't think so. So BACK OFF buckaroo")
            return
        try:
            class DenyModal(discord.ui.Modal, title="Reasoning"):
                def __init__(self, bot, interaction):
                    super().__init__()
                    self.bot = bot
                    self.interaction = interaction

                    self.reason = discord.ui.TextInput(label="reason", style=discord.TextStyle.paragraph)

                    self.add_item(self.reason)

                async def on_submit(self, interaction: discord.Interaction):
                    reason = self.reason.value

                    og_embed = interaction.message.embeds[0]
                    og_description = og_embed.description

                    new_embed = discord.Embed(
                        title=og_embed.title,
                        description=og_description + f"\n\n> - **Denied** <t:{int(datetime.datetime.now().timestamp())}:R>\n> - **Reason:** {reason}",
                        color=og_embed.color
                    )
                    new_embed.set_image(url=og_embed.image.url)

                    await interaction.message.edit(embed=new_embed, view=None, content=None)
                    await interaction.response.send_message(content="Success", ephemeral=True)

            await interaction.response.send_modal(DenyModal(self.bot, interaction))
        except Exception as e:
            print(e)