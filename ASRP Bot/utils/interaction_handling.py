from discord.ext import commands
import discord, config, time, toml

class InteractionHandler(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_interaction(self, interaction: discord.Interaction):
        if interaction.response.is_done():
            return

        if interaction.type == discord.InteractionType.component:
            if interaction.data.get("custom_id") == "dc_reminder":
                await interaction.response.defer(ephemeral=True)

                og_embed = interaction.message.embeds[0]
                embed = discord.Embed(
                    title=og_embed.title,
                    color=discord.Color.from_str(config.colors.LIGHT_GREEN)
                )

                for field in og_embed.fields:
                    embed.add_field(name=field.name, value=field.value, inline=field.inline)

                embed.set_image(url=config.imgs.LIGHT_GREEN_IMG)
                embed.set_footer(text=og_embed.footer.text, icon_url=og_embed.footer.icon_url)
                embed.set_thumbnail(url=config.LOGO)

                view = discord.ui.View()
                view.add_item(
                    discord.ui.Button(label="Discord Check Completed!", style=discord.ButtonStyle.green, disabled=True))

                await interaction.message.edit(content=None, embed=embed, view=view)

            elif interaction.data.get("custom_id") == "session_logging":

                original_embed = interaction.message.embeds[0]
                original_content = original_embed.description

                if " started," in original_embed.title:
                    original_content = original_content.replace("**Action Done:** `SSUed`\n",
                                                                f"**Action Done:** `SSUed`\n> - **Time Confirmed:** {config.current_time()}\n")

                    edited_embed = discord.Embed(
                        description=original_content,
                        title="__<:ServerSSU:1316165992727973948> | The server startup message has been confirmed!__",
                        color=discord.Color.from_str(config.colors.GREEN)
                    )
                    edited_embed.set_footer(text=f"Confirmed by: {interaction.user.nick}",
                                            icon_url=interaction.user.avatar)
                    edited_embed.set_image(url=original_embed.image.url)
                elif "shut down" in original_embed.title:
                    original_content = original_content.replace("**Action Done:** `SSDed`\n",
                                                                f"**Action Done:** `SSDed`\n> - **Time Confirmed:** {config.current_time()}\n")

                    edited_embed = discord.Embed(
                        description=original_content,
                        title="__<:ServerSSD:1316165994124804116> | The server shutdown message has been confirmed!__",
                        color=discord.Color.from_str(config.colors.RED)
                    )
                    edited_embed.set_footer(text=f"Confirmed by: {interaction.user.nick}",
                                            icon_url=interaction.user.avatar)
                    edited_embed.set_image(url=original_embed.image.url)
                elif "Low Player Ping" in original_embed.title:
                    original_content = f"{original_content}\n> - **Time Confirmed:** {config.current_time()}"

                    edited_embed = discord.Embed(
                        description=original_content,
                        title="__<:ServerLLP:1316165989012082708> | The Low Player Ping message has been confirmed!__",
                        color=discord.Color.from_str(config.colors.YELLOW)
                    )
                    edited_embed.set_footer(text=f"Confirmed by: {interaction.user.nick}",
                                            icon_url=interaction.user.avatar)
                    edited_embed.set_image(url=original_embed.image.url)
                elif "Server Restart" in original_embed.title:
                    original_content = f"{original_content}\n> - **Time Confirmed:** {config.current_time()}"

                    edited_embed = discord.Embed(
                        description=original_content,
                        title="__<:ServerRestart:1386846452805931021> | The Server Restart message has been confirmed!__",
                        color=discord.Color.from_str(config.colors.ORANGE)
                    )
                    edited_embed.set_footer(text=f"Confirmed by: {interaction.user.nick}",
                                            icon_url=interaction.user.avatar)
                    edited_embed.set_image(url=original_embed.image.url)
                elif "Server Crash" in original_embed.title:
                    original_content = f"{original_content}\n> - **Time Confirmed:** {config.current_time()}"

                    edited_embed = discord.Embed(
                        description=original_content,
                        title="__<:ServerCrash:1316165991561957447> | The Server Crash message has been confirmed!__",
                        color=discord.Color.from_str(config.colors.GREY)
                    )
                    edited_embed.set_footer(text=f"Confirmed by: {interaction.user.nick}",
                                            icon_url=interaction.user.avatar)
                    edited_embed.set_image(url=original_embed.image.url)
                elif "Server Update" in original_embed.title:
                    original_content = f"{original_content}\n> - **Time Confirmed:** {config.current_time()}"

                    edited_embed = discord.Embed(
                        description=original_content,
                        title="__<:ServerUpdate:1316165989963927645> | The Server Update message has been confirmed!__",
                        color=discord.Color.from_str(config.colors.BLUE)
                    )
                    edited_embed.set_footer(text=f"Confirmed by: {interaction.user.nick}",
                                            icon_url=interaction.user.avatar)
                    edited_embed.set_image(url=original_embed.image.url)

                await interaction.message.edit(embed=edited_embed, view=None)

            elif interaction.data.get("custom_id") == "app_prio":
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

            elif "feedback" in interaction.data.get("custom_id"):
                if interaction.user.name != "wl345":
                    interaction.response.send_message(
                        "Are you WL? I didn't think so. So BACK OFF buckaroo")
                    return

                if "complete" in interaction.data.get("custom_id"):
                    og_embed = interaction.message.embeds[0]
                    og_description = og_embed.description

                    new_embed = discord.Embed(
                        title=og_embed.title,
                        description=og_description + f"\n\n> - **Completed** {config.current_time()}",
                        color=discord.Color.from_str(config.colors.LIGHT_GREEN)
                    )
                    new_embed.set_image(url=config.imgs.LIGHT_GREEN_IMG)
                    await interaction.message.edit(embed=new_embed, view=None, content=None)

                elif "deny" in interaction.data.get("custom_id"):
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

            elif "ban-bolo" in interaction.data.get("custom_id"):
                if "automated" in interaction.data.get("custom_id"):
                    await interaction.response.send_message("This is not currently a function! Please use the manual button instead!", ephemeral=True)

                elif "manual" in interaction.data.get("custom_id"):
                    try:
                        from cogs.ban_bolo import CompletionButton
                        og_desc = interaction.message.embeds[0].description
                        for line in og_desc.splitlines():
                            if line.startswith("> - **Requested to Ban:** [`"):
                                roblox_id = line.split("`")[1].strip()
                                break

                        data = toml.load("storage/misc.toml")
                        log_msg = data["interactions"]["ban-bolo"][roblox_id]

                        embed = discord.Embed(
                            title="Manual Ban-Bolo Message!",
                            description=f"You **MUST** either be in game, able to run the command, or able to use Melonly to remotely ban them.\n```:ban {roblox_id}```",
                            color=discord.Color.from_str(config.colors.LIGHT_BLUE)
                        )

                        view = CompletionButton(log_msg, interaction.message, self.bot, roblox_id)
                        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)

                    except Exception as e:
                        print(e)

            elif "chatmod" in interaction.data.get("custom_id"):
                try:
                    og_embed = interaction.message.embeds[0]
                    new_embed = discord.Embed(
                        title="Chatmod Request Completed!",
                        description=og_embed.description + f"\n\n> - **Completed By:** {interaction.user.mention}\n> - **Completed** {config.current_time()}",
                        color=discord.Color.from_str(config.colors.LIGHT_GREEN)
                    )
                    new_embed.set_footer(text=f"Completed By: {interaction.user.nick}",
                                         icon_url=interaction.user.avatar.url)
                    new_embed.set_image(url=config.imgs.LIGHT_GREEN_IMG)

                    view = discord.ui.View.from_message(interaction.message)
                    for item in view.children:
                        if isinstance(item, discord.ui.Button) and item.label == "Mark as Complete!":
                            view.remove_item(item)

                    new_log_embed = discord.Embed(
                        title=new_embed.title,
                        description=new_embed.description,
                        color=new_embed.color
                    )
                    new_log_embed.set_footer(text="Alaska State Roleplay - Automated Logging System",
                                             icon_url=interaction.user.avatar.url)
                    new_log_embed.set_image(url=config.imgs.LIGHT_GREEN_IMG)

                    data = toml.load("storage/misc.toml")
                    log_msg = data["interactions"]["chatmod"][str(interaction.message.id)]
                    del data["interactions"]["chatmod"][str(interaction.message.id)]
                    with open("storage/misc.toml", "w") as f:
                        toml.dump(data, f)

                    await interaction.message.edit(embed=new_embed, view=view, content=None)
                    log_msg = await self.bot.get_channel(config.channels.DM_CHAT).fetch_message(log_msg)
                    await log_msg.edit(embed=new_log_embed)

                    await interaction.response.defer(ephemeral=True)
                except Exception as e:
                    print(e)



# Required setup function
async def setup(bot):
    await bot.add_cog(InteractionHandler(bot))
