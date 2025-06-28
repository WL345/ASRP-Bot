import discord.ext


class move_trainingCog(discord.ext.commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # @discord.app_commands.guilds(discord.Object(id=1182487341386969158))
    @discord.app_commands.command(name="transfer-training", description="Change a support ticket into a training channel (temporary command)")
    @discord.app_commands.describe(channel="What is the channel ID of the ticket to transfer?")
    async def move_training(self, interaction: discord.Interaction, channel: discord.TextChannel):

        tm_sv = self.bot.get_guild(1182487341386969158).get_role(1182827710855254056)
        dmt = self.bot.get_guild(1182487341386969158).get_role(1182827695537672322)

        sv_overwrite = channel.overwrites_for(tm_sv)
        sv_overwrite.send_messages = True
        sv_overwrite.view_channel = True

        dmt_overwrite = channel.overwrites_for(dmt)
        dmt_overwrite.view_channel = False

        # await channel.set_permissions(tm_sv, overwrite=sv_overwrite)
        # await channel.set_permissions(dmt, overwrite=dmt_overwrite)
        await channel.send("<@&1182827710855254056>")
        await interaction.response.send_message(f"Successfully changed <#{channel.id}> into a training ticket"
                                                f"\n-# If this link does not appear as #No Access, something has gone wrong! (unless you're using Vencord)", ephemeral=Truetdis)


async def setup(bot):
    await bot.add_cog(move_trainingCog(bot))
