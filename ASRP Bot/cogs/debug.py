import discord.ext

class debugCog(discord.ext.commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name="debug", description="For Debugging purposes.")
    @discord.app_commands.describe(choice="pick an option")
    @discord.app_commands.choices(
        choice=[
            discord.app_commands.Choice(name="1", value="1182828263828103240"),
            discord.app_commands.Choice(name="2", value="1387845894182797555"),
            discord.app_commands.Choice(name="3", value="1387913096680706158")
        ]
    )
    # 555 - thread  ####  158 - astro ticket   ####   240 - mgmt chat

    async def debug(self, interaction: discord.Interaction, choice: str):
        if interaction.user.name != "wl345":
            await interaction.response.send_message("https://tenor.com/view/this-is-not-for-you-rudy-ayoub-this-aint-for-you-its-not-intended-for-you-gif-27340083", ephemeral=True)
            return

        messages = []

        async for msg in self.bot.get_channel(int(choice)).history(limit=50):
            author = str(msg.author)
            content = msg.content.strip()
            if content:
                messages.append(f"{author} - {content}")

        output = "\n".join(messages)
        await self.bot.get_channel(1349948550460735509).send(output[:2000])
        await interaction.response.send_message("https://discord.com/channels/1292670781926408202/1349948550460735509", ephemeral=True)

async def setup(bot):
    await bot.add_cog(debugCog(bot))
