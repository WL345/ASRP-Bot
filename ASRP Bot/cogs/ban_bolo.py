import discord.ext, config


class BoloButtons(discord.ui.View):
    def __init__(self, log_msg, roblox_id):
        super().__init__()
        self.log_msg = log_msg
        self.roblox_id = roblox_id

    @discord.ui.button(label="Automated Ban-Bolo", style=discord.ButtonStyle.blurple)
    async def automated(self, button_interaction: discord.Interaction, button: discord.ui.Button):
        await button_interaction.response.send_message(
            "This is not currently a function! Please use the manual button instead!", ephemeral=True)

    @discord.ui.button(label="Manual Ban-Bolo", style=discord.ButtonStyle.blurple)
    async def manual(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            embed = discord.Embed(
                title="Manual Ban-Bolo Message!",
                description=f"You **MUST** either be in game, able to run the command, or able to use Melonly to remotely ban them.\n```:ban {self.roblox_id}```",
                color=discord.Color.from_str(config.colors.LIGHT_BLUE)
            )

            view = CompletionButton(self.log_msg, interaction.message)
            await interaction.response.send_message(embed=embed, view=view, ephemeral=True)

        except Exception as e:
            print(e)

class CompletionButton(discord.ui.View):
    def __init__(self, log_msg, req_msg):
        super().__init__()
        self.log_msg = log_msg
        self.req_msg = req_msg

    @discord.ui.button(label="Mark As Complete!", style=discord.ButtonStyle.green)
    async def completed(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            og_embed = self.req_msg.embeds[0]

            edit_embed = discord.Embed(
                title="Ban-Bolo Request Completed!",
                description=og_embed.description + f"\n> - **Completed** {config.current_time()}",
                color=discord.Color.from_str(config.colors.LIGHT_GREEN)
            )
            edit_embed.set_image(url=og_embed.image.url)
            edit_embed.set_thumbnail(url=og_embed.thumbnail.url)
            edit_embed.set_footer(text=f"Manually Completed by: {interaction.user.nick}",
                                  icon_url=interaction.user.avatar.url)

            edit_log_embed = discord.Embed(
                title=edit_embed.title,
                description=edit_embed.description,
                color=edit_embed.color
            )

            completed_button = discord.ui.Button(label="Manually Completed!", style=discord.ButtonStyle.green, disabled=True)
            view = discord.ui.View()
            view.add_item(completed_button)

            edit_log_embed.set_thumbnail(url=edit_embed.thumbnail.url)
            edit_log_embed.set_image(url=edit_embed.image.url)
            edit_log_embed.set_footer(text=edit_embed.footer.text, icon_url=edit_embed.footer.icon_url)

            await self.req_msg.edit(content=None, embed=edit_embed, view=view)
            await self.log_msg.edit(embed=edit_log_embed)
            await interaction.response.edit_message(content="Successfully completed that bolo request!", embed=None, view=None)


        except Exception as e:
            print(e)

class BanBoloCog(discord.ext.commands.Cog):
    def __init__(self, bot):
        self.bot: discord.ext.commands.Bot = bot

    @discord.app_commands.command(name="ban-bolo", description="Create a ban bolo for an Admin to check!")
    @discord.app_commands.describe(roblox_id="The ROBLOX ID of the user you need banned.", ban_length="The length of the user being banned. (Ex. 3d, 5d, 7d)", screenshot="Screenshot of the ban-bolo in Melonly.")
    async def get_user_id(self, interaction: discord.Interaction, roblox_id: str, ban_length: str, screenshot: discord.Attachment):
        print(f"\n{interaction.user.name} - <@{interaction.user.id}> - Used the Bolo command")


        embed = discord.Embed(
            title="Ban-Bolo Request!",
            description=f"""
> - **Requested By:** {interaction.user.mention}
> - **Requested to Ban:** [`{roblox_id}`](https://www.roblox.com/users/{roblox_id}/profile)
> - **Ban Time:** `{ban_length}`
> - **Requested** {config.current_time()}""",
            color=discord.Color.from_str(config.colors.LIGHT_BLUE)
        )
        embed.set_thumbnail(url=config.LOGO)
        embed.set_image(url=screenshot.url)
        embed.set_footer(text="Click a button below, please note the server must be up for the automatic button to work.", icon_url=config.LOGO)

        logging_embed = discord.Embed(
            title=embed.title,
            description=embed.description,
            color=embed.color
        )
        logging_embed.set_thumbnail(url=embed.thumbnail.url)
        logging_embed.set_image(url=embed.image.url)

        log_msg = await self.bot.get_channel(config.channels.BOLO_LOGGING).send(embed=logging_embed)
        view = BoloButtons(log_msg, roblox_id)
        req_msg = await self.bot.get_channel(config.channels.ADMIN_REQUESTS).send("<@&1182827674599706624>", embed=embed, view=view)
        await interaction.response.send_message("Successfully created a ban-bolo request.", ephemeral=True)


async def setup(bot):
    await bot.add_cog(BanBoloCog(bot))
