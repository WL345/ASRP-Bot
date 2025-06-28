import discord.ext, datetime
from config import DM_LOGGING_CHANNEL
from utils.colors import colors

class DMCog(discord.ext.commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # @discord.app_commands.guilds(discord.Object(id=1182487341386969158))
    @discord.app_commands.command(name="dm", description="DM a user of your choice, anonymously.")
    @discord.app_commands.describe(user="The user you want to DM.", message="The message you want to send.")
    async def get_user_id(self, interaction: discord.Interaction, user: discord.User, message: str):
        try:
            await user.send(message)
            await interaction.response.send_message(f":white_check_mark: Successfully DMed {user.mention}.", ephemeral=True)

            embed = discord.Embed(
                title="__Someone DMed Someone!__",
                description=f"""
> - **Used By:** {interaction.user.mention}
> - **DMed:** {user.mention}
> - **Time Used:** <t:{int(datetime.datetime.now().timestamp())}:R>
> - **Message Content:** `{message}`
""",
                color=discord.Color.from_str(colors.LIGHT_BLUE)
            )

            embed.set_footer(text="ASRP - Automated Command Logging System", icon_url="https://media.discordapp.net/attachments/1182828263828103240/1183834014465925130/file-z2wbRRQ45BNH3lmnqqBb4L3M_1.png?ex=685edf57&is=685d8dd7&hm=148d736a4c74c422ce644226ce2bd0646fbc3a6dca16ea7f238e77c57113fe1c&")
            embed.set_image(url="https://cdn.discordapp.com/attachments/1182828263828103240/1288246137156796542/Untitled.png?ex=685f08b5&is=685db735&hm=10e057c8a919280ed03d5a16341752f18da85457de1c7b1504784b3f9c6bf143&")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1182828263828103240/1183834014465925130/file-z2wbRRQ45BNH3lmnqqBb4L3M_1.png?ex=685edf57&is=685d8dd7&hm=148d736a4c74c422ce644226ce2bd0646fbc3a6dca16ea7f238e77c57113fe1c&")

            await self.bot.get_channel(DM_LOGGING_CHANNEL).send(embed=embed)

        except Exception as e:
            await interaction.response.send_message(f"I was unable to DM {user.mention}. This is the error I recieved - \n```{e}```")


async def setup(bot):
    await bot.add_cog(DMCog(bot))
