import discord, datetime
from config import FEEDBACK_CHANNEL
from utils.colors import colors
from utils.feedback_views import MarkFeedbackComplete


class FeedbackCog(discord.ext.commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # @discord.app_commands.guilds(discord.Object(id=1182487341386969158))
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
        embed = discord.Embed(
            title="New ASRP Bot Feedback!",
            description=f"""
> - **User Information:**
>    - **Suggested By:** {interaction.user.mention} (`{interaction.user.id}`)
>    - **Suggested** <t:{int(datetime.datetime.now().timestamp())}:R>

> - **Feedback Information:**
>    - **Feedback Type:** `{feedback_type}`
>    - **Feedback:** ```{feedback}```
""",
            color=discord.Color.from_str(colors.LIGHT_BLUE)
        )

        embed.set_image(url="https://cdn.discordapp.com/attachments/1182828263828103240/1288246137156796542/Untitled.png?ex=686102f5&is=685fb175&hm=92f0f4134778bc3d0f9882c4b322674d9ac26abf48a8a2df62d90e0ce7a271e0&")

        view = MarkFeedbackComplete(self.bot)
        await self.bot.get_channel(FEEDBACK_CHANNEL).send(content="<@995686080030445578>", embed=embed, view=view)
        await interaction.response.send_message("Your feedback has been sent successfully. Thank you!", ephemeral=True)

async def setup(bot):
    await bot.add_cog(FeedbackCog(bot))
