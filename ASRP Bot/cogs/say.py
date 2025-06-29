from discord.ext import commands
import discord

class SayCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name="say", description="Say something as the bot.")
    @discord.app_commands.describe(message="message", id="id")
    async def say(self, interaction: discord.Interaction, message: str, id: str = None):
        print(f"{interaction.user.name} - <@{interaction.user.id}> - Used the say command")
        if id:
            channel = await self.bot.fetch_channel(interaction.channel.id)
            reply_to = await channel.fetch_message(id)
            await reply_to.reply(message, mention_author=False)
        else:
            await interaction.channel.send(content=message)
        await interaction.response.send_message("Success", ephemeral=True)


async def setup(bot):
    await bot.add_cog(SayCog(bot))
