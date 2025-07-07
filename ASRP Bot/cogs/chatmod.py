import discord.ext, config


class ChatmodCog(discord.ext.commands.Cog):
    def __init__(self, bot):
        self.bot: discord.ext.commands.Bot = bot

    @discord.app_commands.command(name="chatmod", description="Call for a Discord Moderator!")
    @discord.app_commands.describe(reporting="Who are you requesting a chatmod to deal with?", reasoning="Why are you requesting a chatmod?", message="The link to the message you are reporting")
    async def get_user_id(self, interaction: discord.Interaction, reporting: discord.User, reasoning: str, message: str):
        print(f"\n{interaction.user.name} - <@{interaction.user.id}> - Used the chatmod command")

        if message.startswith("https://discord.com/channels/1182487341386969158"):
            pass
        else:
            await interaction.response.send_message("That is not a proper message link!", ephemeral=True)
            return

        try:

            class CompletedButton(discord.ui.View):
                @discord.ui.button(label="Competed!", style=discord.ButtonStyle.green, emoji="✔️")
                async def completed(self, interaction: discord.Interaction, button: discord.Button):
                    try:
                        og_embed = interaction.message.embeds[0]
                        new_embed = discord.Embed(
                            title="Chatmod Request Completed!",
                            description=og_embed.description + f"\n\n> - **Completed By:** {interaction.user.mention}\n> - **Completed** {config.current_time()}",
                            color=discord.Color.from_str(config.colors.LIGHT_GREEN)
                        )
                        new_embed.set_footer(text=f"Completed By: {interaction.user.nick}", icon_url=interaction.user.avatar.url)
                        new_embed.set_image(url=config.imgs.LIGHT_GREEN_IMG)

                        link = discord.ui.Button(label="Jump to Message!", emoji="🔗", url=message)
                        view = discord.ui.View()
                        view.add_item(link)

                        new_log_embed = discord.Embed(
                            title=new_embed.title,
                            description=new_embed.description,
                            color=new_embed.color
                        )
                        new_log_embed.set_footer(text="Alaska State Roleplay - Automated Logging System", icon_url=interaction.user.avatar.url)
                        new_log_embed.set_image(url=config.imgs.LIGHT_GREEN_IMG)

                        await interaction.message.edit(embed=new_embed, view=view, content=None)
                        await log_msg.edit(embed=new_log_embed)

                        await interaction.response.send_message("Successfully marked it as completed!", ephemeral=True)

                    except Exception as e:
                        print(e)

            embed = discord.Embed(
                title=f"{interaction.user.nick} has requested a chatmod!",
                description=f"""
    > - **Requested by:** {interaction.user.mention}
    > - **Reporting:** {reporting.mention}
    > - **Reason for Chatmod:** {reasoning}
    > - **Requested in:** <#{interaction.channel.id}>
    > - **Requested** {config.current_time()}""",
                color=discord.Color.from_str(config.colors.LIGHT_BLUE)
            )
            embed.set_footer(text="Click \"Completed\" once the user has been dealt with!", icon_url=config.LOGO)
            embed.set_image(url=config.imgs.LIGHT_BLUE_IMG)
            embed.set_thumbnail(url=config.LOGO)

            link = discord.ui.Button(label="Jump to Message!", emoji="🔗", url=message)
            view = CompletedButton()
            view.add_item(link)

            logging_embed = discord.Embed(
                title=embed.title,
                description=embed.description,
                color=embed.color
            )
            logging_embed.set_footer(text="Alaska State Roleplay - Automated Logging System")
            logging_embed.set_image(url=config.imgs.LIGHT_BLUE_IMG)
            logging_embed.set_thumbnail(url=config.LOGO)

            await self.bot.get_channel(config.channels.DM_CHAT).send("<@&1182827695537672322>", embed=embed, view=view)
            log_msg = await self.bot.get_channel(config.channels.CHATMOD_LOGGING).send(embed=logging_embed)

            await interaction.response.send_message(f"Successfully requested a chatmod for {reporting.mention}.", ephemeral=True)

        except Exception as e:
            print(e)

async def setup(bot):
    await bot.add_cog(ChatmodCog(bot))
