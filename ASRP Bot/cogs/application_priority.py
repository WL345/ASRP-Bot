import discord.ext, datetime, config

class AppPrioCog(discord.ext.commands.Cog):
    def __init__(self, bot):
        self.bot: discord.ext.commands.Bot = bot

    @discord.app_commands.command(name="application-priority", description="Claim your application priority perk!")
    @discord.app_commands.describe(application="Which application are you claiming your perk on?")
    @discord.app_commands.choices(application=[
        discord.app_commands.Choice(name="In-Game Staff", value="In-Game Staff"),
        discord.app_commands.Choice(name="Discord Staff", value="Discord Staff")
        ]
    )
    async def get_user_id(self, interaction: discord.Interaction, application: str):
        print(f"\n{interaction.user.name} - <@{interaction.user.id}> - Used the application priority command")

        class CompletionButton(discord.ui.View):
            def __init__(self, bot):
                super().__init__()
                self.bot: discord.ext.commands.Bot = bot

            @discord.ui.button(label="Completed", emoji="<:Check:1209512754465996860>", style=discord.ButtonStyle.green)
            async def completion(self, interaction: discord.Interaction, button: discord.ui.Button):
                try:

                    og_embed = interaction.message.embeds[0]
                    embed = discord.Embed(
                        title="A priority application has been read!",
                        description=og_embed.description + f"\n\n> **Completed By: {interaction.user.mention}**\n> **Completed:** {config.current_time()}",
                        color=og_embed.color
                    )
                    embed.set_footer(text=og_embed.footer.text, icon_url=og_embed.footer.icon_url)
                    embed.set_thumbnail(url=og_embed.thumbnail.url)
                    embed.set_image(url=og_embed.image.url)

                    await interaction.message.edit(content=None, embed=embed, view=None)
                except Exception as e:
                    print(e)

        embed = discord.Embed(
            title="A user has used their application priority perk!",
            description=f"""
> **Applicants Username:** {interaction.user.mention}
> **Time:** {config.current_time()}
> **Next Perk:** <t:{int((datetime.datetime.now() + datetime.timedelta(days=31)).timestamp())}:R>
> **Application:** {application}""",
            color=discord.Color.from_str(config.colors.LIGHT_BLUE)
        )
        embed.set_footer(text="Alaska State Roleplay - Application Priority System", icon_url="https://media.discordapp.net/attachments/1182828263828103240/1183834014465925130/file-z2wbRRQ45BNH3lmnqqBb4L3M_1.png?ex=68637c97&is=68622b17&hm=9568dec8404d2a17d70a813a1e0f4048eb142110e666ee01541b0ae9c320a36b&")
        embed.set_image(url=config.imgs.LIGHT_BLUE_IMG)
        embed.set_thumbnail(url=config.LOGO)

        view = CompletionButton(self.bot)
        await self.bot.get_channel(config.channels.APPLICATION_PRIO).send("[staff manager ping - 1354933462892548257]", embed=embed, view=view)
        await interaction.response.send_message(f"Successfully requested application priority! Your {application} application will be read soon.", ephemeral=True)

async def setup(bot):
    await bot.add_cog(AppPrioCog(bot))
