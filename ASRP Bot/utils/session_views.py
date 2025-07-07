import traceback, discord, config
from config import *
from utils.timed_events import start_reminders, stop_reminders


class FinalLogConfirmation(discord.ui.View):
    def __init__(self, session_type):
        super().__init__()
        self.session_type = session_type

    @discord.ui.button(label="Confirm", style=discord.ButtonStyle.green)
    async def confirm_log(self, interaction: discord.Interaction, button: discord.ui.Button):

        original_embed = interaction.message.embeds[0]
        original_content = original_embed.description
        if self.session_type == "ssu":
            original_content = original_content.replace("**Action Done:** `SSUed`\n", f"**Action Done:** `SSUed`\n> - **Time Confirmed:** {config.current_time()}\n")

            edited_embed = discord.Embed(
                description=original_content,
                title="__<:ServerSSU:1316165992727973948> | The server startup message has been confirmed!__",
                color=discord.Color.from_str(config.colors.GREEN)
            )
            edited_embed.set_footer(text=f"Confirmed by: {interaction.user.nick}", icon_url=interaction.user.avatar)
            edited_embed.set_image(url=imgs.GREEN_SESSION_IMG)

        elif self.session_type == "ssd":
            original_content = original_content.replace("**Action Done:** `SSDed`\n", f"**Action Done:** `SSDed`\n> - **Time Confirmed:** {config.current_time()}\n")

            edited_embed = discord.Embed(
                description=original_content,
                title="__<:ServerSSD:1316165994124804116> | The server shutdown message has been confirmed!__",
                color=discord.Color.from_str(config.colors.RED)
            )
            edited_embed.set_footer(text=f"Confirmed by: {interaction.user.nick}", icon_url=interaction.user.avatar)
            edited_embed.set_image(url=imgs.RED_SESSION_IMG)

        elif self.session_type == "lpp":
            original_content = f"{original_content}\n> - **Time Confirmed:** {config.current_time()}"

            edited_embed = discord.Embed(
                description=original_content,
                title="__<:ServerLLP:1316165989012082708> | The Low Player Ping message has been confirmed!__",
                color=discord.Color.from_str(config.colors.YELLOW)
            )
            edited_embed.set_footer(text=f"Confirmed by: {interaction.user.nick}", icon_url=interaction.user.avatar)
            edited_embed.set_image(url=imgs.YELLOW_SESSION_IMG)

        elif self.session_type == "restart":
            original_content = f"{original_content}\n> - **Time Confirmed:** {config.current_time()}"

            edited_embed = discord.Embed(
                description=original_content,
                title="__<:ServerRestart:1386846452805931021> | The Server Restart message has been confirmed!__",
                color=discord.Color.from_str(config.colors.ORANGE)
            )
            edited_embed.set_footer(text=f"Confirmed by: {interaction.user.nick}", icon_url=interaction.user.avatar)
            edited_embed.set_image(url=imgs.ORANGE_SESSION_IMG)

        elif self.session_type == "crash":
            original_content = f"{original_content}\n> - **Time Confirmed:** {config.current_time()}"

            edited_embed = discord.Embed(
                description=original_content,
                title="__<:ServerCrash:1316165991561957447> | The Server Crash message has been confirmed!__",
                color=discord.Color.from_str(config.colors.GREY)
            )
            edited_embed.set_footer(text=f"Confirmed by: {interaction.user.nick}", icon_url=interaction.user.avatar)
            edited_embed.set_image(url=imgs.GREY_SESSION_IMG)

        elif self.session_type == "update":
            original_content = f"{original_content}\n> - **Time Confirmed:** {config.current_time()}"

            edited_embed = discord.Embed(
                description=original_content,
                title="__<:ServerUpdate:1316165989963927645> | The Server Update message has been confirmed!__",
                color=discord.Color.from_str(config.colors.BLUE)
            )
            edited_embed.set_footer(text=f"Confirmed by: {interaction.user.nick}", icon_url=interaction.user.avatar)
            edited_embed.set_image(url=imgs.BLUE_SESSION_IMG)

        await interaction.message.edit(embed=edited_embed, view=None)
class SessionConfirmationView(discord.ui.View):
    def __init__(self, bot, session_type: str):
        super().__init__()
        self.bot = bot
        self.session_type = session_type

    @discord.ui.button(label="Confirm", style=discord.ButtonStyle.green)
    async def confirm(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.session_type == "ssu":
            await interaction.response.send_modal(SSUModal(self.bot, interaction))
            return

        elif self.session_type == "ssd":
            await interaction.response.send_modal(SSDModal(self.bot, interaction))
            return

        elif self.session_type == "lpp":
            try:
                embed = discord.Embed(
                    title="__<:ServerLLP:1316165989012082708> | Low Player Ping!__",
                    description=f"""
> - We are currently low on players on the server. Please join to prevent a server shutdown earlier than expected. prior to joining, we suggest that you review our [game rules.](https://discord.com/channels/1182487341386969158/1182828141656424468)

> - **Server Name:** Alaska State Roleplay
> - **Server Owner:** Bobsquad16
> - **Server Code: [ALASKA](https://policeroleplay.community/join?code=ALASKA&placeId=2534724415)**
> - **Sent By: {interaction.user.mention}**

> Low player notice announced {config.current_time()}.
""",
                    color=discord.Color.from_str(config.colors.YELLOW)
                )
                embed.set_image(url=imgs.YELLOW_SESSION_IMG)
                embed.set_footer(text="Have any questions? Make a support ticket!",
                                 icon_url=config.LOGO)
                embed.set_thumbnail(
                    url=config.LOGO)

                log_embed = discord.Embed(
                    title="<:ServerLLP:1316165989012082708> | __The Low Player Ping has been sent, please confirm below!__",
                    description=f"> - **Sent By:** <@{interaction.user.id}>\n> - **Time Sent:** {config.current_time()}\n> - **Action Done:** `LLP`",
                    color=discord.Color.from_str(config.colors.YELLOW)
                )
                log_embed.set_image(
                    url=imgs.YELLOW_SESSION_IMG)

            except Exception as e:
                print(f"llp sending error - {e}")

        elif self.session_type == "restart":
            try:
                embed = discord.Embed(
                    title="__<:ServerRestart:1386846452805931021> | Server Restart!__",
                    description=f"""
> - We have restarted our in-game server, either due to mass amounts of lag, failure to RP, or another reason. Feel free to rejoin!

> - **Server Name:** Alaska State Roleplay
> - **Server Owner:** Bobsquad16
> - **Server Code: [ALASKA](https://policeroleplay.community/join?code=ALASKA&placeId=2534724415)**
> - **Sent By: {interaction.user.mention}**

> This session was restarted {config.current_time()}.""",
                    color=discord.Color.from_str(config.colors.ORANGE)
                )
                embed.set_image(url=imgs.ORANGE_SESSION_IMG)
                embed.set_footer(text="Have any questions? Make a support ticket!",
                                 icon_url=config.LOGO)
                embed.set_thumbnail(
                    url=config.LOGO)

                log_embed = discord.Embed(
                    title="<:ServerRestart:1386846452805931021> | __The Server Restart message has been sent, please confirm below!__",
                    description=f"> - **Sent By:** <@{interaction.user.id}>\n> - **Time Sent:** {config.current_time()}\n> - **Action Done:** `Restart`",
                    color=discord.Color.from_str(config.colors.ORANGE)
                )
                log_embed.set_image(
                    url=imgs.ORANGE_SESSION_IMG)

            except Exception as e:
                print(f"restart sending error - {e}")

        elif self.session_type == "crash":
            try:
                embed = discord.Embed(
                    title="__<:ServerCrash:1316165991561957447> | Server Crash!__",
                    description=f"""
> - Our in-game server has crashed! Please feel free to rejoin and continue your roleplays, we apologize for any inconveniences!

> - **Server Name:** Alaska State Roleplay
> - **Server Owner:** Bobsquad16
> - **Server Code: [ALASKA](https://policeroleplay.community/join?code=ALASKA&placeId=2534724415)**
> - **Sent By: {interaction.user.mention}**

> This session crashed {config.current_time()}.""",
                    color=discord.Color.from_str(config.colors.GREY)
                )
                embed.set_image(url=imgs.GREY_SESSION_IMG)
                embed.set_footer(text="Have any questions? Make a support ticket!",
                                 icon_url=config.LOGO)
                embed.set_thumbnail(
                    url=config.LOGO)

                log_embed = discord.Embed(
                    title="<:ServerCrash:1316165991561957447>> | __The Server Crash message has been sent, please confirm below!__",
                    description=f"> - **Sent By:** <@{interaction.user.id}>\n> - **Time Sent:** {config.current_time()}\n> - **Action Done:** `Crash`",
                    color=discord.Color.from_str(config.colors.GREY)
                )
                log_embed.set_image(
                    url=imgs.GREY_SESSION_IMG)

            except Exception as e:
                print(f"crash sending error - {e}")

        elif self.session_type == "update":
            try:
                embed = discord.Embed(
                    title="__<:ServerUpdate:1316165989963927645> | PRC Update!__",
                    description=f"""
> - Our hosting game, Emergency Response; Liberty County, has updated. As such, the server has been restarted. Feel free to rejoin the server, and continue your roleplays.

> - **Server Name:** Alaska State Roleplay
> - **Server Owner:** Bobsquad16
> - **Server Code: [ALASKA](https://policeroleplay.community/join?code=ALASKA&placeId=2534724415)**
> - **Sent By: {interaction.user.mention}**

> This session updated {config.current_time()}.
""",
                    color=discord.Color.from_str(config.colors.BLUE)
                )
                embed.set_image(url=imgs.BLUE_SESSION_IMG)
                embed.set_footer(text="Have any questions? Make a support ticket!",
                                 icon_url=config.LOGO)
                embed.set_thumbnail(
                    url=config.LOGO)


                log_embed = discord.Embed(
                    title="<:ServerUpdate:1316165989963927645> | __The Server Update message has been sent, please confirm below!__",
                    description=f"> - **Sent By:** <@{interaction.user.id}>\n> - **Time Sent:** {config.current_time()}\n> - **Action Done:** `Update`",
                    color=discord.Color.from_str(config.colors.BLUE)
                )
                log_embed.set_image(
                    url=imgs.BLUE_SESSION_IMG)


            except Exception as e:
                print(f"update sending error - {e}")

        button = discord.ui.Button(label="Join Server!", url="https://policeroleplay.community/join?code=ALASKA&placeId=2534724415", emoji="<:events:1261753313842565200>", style=discord.ButtonStyle.link)
        view = discord.ui.View()
        view.add_item(button)

        await self.bot.get_channel(config.channels.SERVER_STATUS).send("@her e <@&1182908708821401631", embed=embed, delete_after=1800, view=view)
        await self.bot.get_channel(config.channels.SESSION_LOGGING).send(
            content="<@&1354551020956549303",
            embed=log_embed,
            view=FinalLogConfirmation(session_type=self.session_type)
        )
        await interaction.response.edit_message(content=f"Successfully sent the {self.session_type} message.", view=None, embed=None)

        self.stop()

    @discord.ui.button(label="Cancel", style=discord.ButtonStyle.red)
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.edit_original_response(embed=discord.Embed(description="Action Canceled."), view=None)
        self.stop()

class SSUModal(discord.ui.Modal, title="SSUers"):
    def __init__(self, bot, interaction):
        super().__init__()
        self.bot = bot
        self.interaction = interaction

        self.user1 = discord.ui.TextInput(label="SSUer #1", style=discord.TextStyle.short, required=True)
        self.user2 = discord.ui.TextInput(label="SSUer #2", style=discord.TextStyle.short, required=False)

        self.add_item(self.user1)
        self.add_item(self.user2)

    async def on_submit(self, interaction: discord.Interaction):
        try:
            user1 = self.user1.value
            user2 = self.user2.value

            embed = discord.Embed(
                title="__<:ServerSSU:1316165992727973948> | Server Startup!__",
                url="https://policeroleplay.community/join?code=ALASKA&placeId=2534724415",
                description=f"""
        > We are now hosting a session! Join our server to engage with our realistic and enjoyable roleplays. We suggest you review our [game rules](https://discord.com/channels/1182487341386969158/1182828141656424468) before joining the server.
        
        > - **Server Name:** Alaska State Roleplay  
        > - **Server Owner:** Bobsquad16  
        > - **Server Code: [ALASKA](https://policeroleplay.community/join?code=ALASKA&placeId=2534724415)**
        > - **Started By:** <@{interaction.user.id}>
        
        > This session has been open since {config.current_time()}
        """,
                color=discord.Color.from_str(config.colors.GREEN)
            )
            embed.set_image(
                url=imgs.GREEN_SESSION_IMG)
            embed.set_thumbnail(
                url=config.LOGO)
            embed.set_footer(
                text="Have any questions? Make a support ticket!",
                icon_url=config.LOGO
            )

            log_embed = discord.Embed(
                title="<:ServerSSU:1316165992727973948> | __The server has been started, please confirm below!__",
                description=f"> - **Sent By:** <@{interaction.user.id}>\n> - **Time Sent:** {config.current_time()}\n> - **Action Done:** `SSUed`\n"
                            f"\n**__SSUer(s):__**\n> - {user1}\n> - {user2}",
                color=discord.Color.from_str(config.colors.GREEN)
            )
            log_embed.set_image(
                url=imgs.GREEN_SESSION_IMG)

            from config import SSD_ID
            channel = self.bot.get_channel(config.channels.SERVER_STATUS)
            msg = await channel.fetch_message(SSD_ID)

            button = discord.ui.Button(label="Join Server!", url="https://policeroleplay.community/join?code=ALASKA&placeId=2534724415", emoji="<:events:1261753313842565200>", style=discord.ButtonStyle.link)
            view = discord.ui.View()
            view.add_item(button)

            await msg.delete()
            ssu_msg = await self.bot.get_channel(config.channels.SERVER_STATUS).send("<@&1182908708821401631", embed=embed, view=view)
            await self.bot.get_channel(config.channels.SESSION_LOGGING).send(content="<@&1354551020956549303", embed=log_embed, view=FinalLogConfirmation("ssu"))
            await self.interaction.edit_original_response(view=None)
            await interaction.response.send_message(
                content="Successfully SSUed!",
                ephemeral=True
            )
            config.session_status = "ssu"
            config.SSU_ID = ssu_msg.id
            # await self.interaction.edit_original_response(content="Successfully SSUed! Please check https://discord.com/channels/1182487341386969158/1187789091459305512 and complete any requests made.", embed=None, view=None)
            # start_reminders()

        except Exception as e:
            print(f"ssu modal error - {e}")

class SSDModal(discord.ui.Modal, title="SSD Reasoning"):
    def __init__(self, bot, interaction):
        super().__init__()
        self.bot = bot
        self.interaction = interaction

        self.reason = discord.ui.TextInput(label="Reason", placeholder="Why are you SSDing?", style=discord.TextStyle.long, required=True)
        self.user = discord.ui.TextInput(label="User(s)", placeholder="Who is requesting the SSD?", style=discord.TextStyle.short, required=True)
        self.other_staff = discord.ui.TextInput(label="Other Staff", placeholder="Were there other staff in-game?", style=discord.TextStyle.short, required=True)
        self.melonly = discord.ui.TextInput(label="Melonly Staff Request", placeholder="Did you use the Melonly staff request?", style=discord.TextStyle.short, required=True)
        self.anything_else = discord.ui.TextInput(label="Anything else?", style=discord.TextStyle.short, required=False)

        self.add_item(self.reason)
        self.add_item(self.user)
        self.add_item(self.other_staff)
        self.add_item(self.melonly)
        self.add_item(self.anything_else)

    async def on_submit(self, interaction: discord.Interaction):
        try:
            reason, user, other_staff, melonly, anything_else = self.reason, self.user, self.other_staff, self.melonly, self.anything_else

            embed = discord.Embed(
                title="__<:ServerSSD:1316165994124804116> | Server Shutdown!__",
                description=f"""
                    > - Our server has shut down. Another server startup will be hosted when sufficient staff are available to host. Please do not join the server during a shutdown, thank you for playing on Alaska State Roleplay!
    
                    > This session shutdown {config.current_time()}.
                    """,
                color=discord.Color.from_str(config.colors.RED)
        )
            embed.set_footer(text="Have any questions? Make a support ticket!", icon_url=config.LOGO)
            embed.set_image(url=config.imgs.RED_SESSION_IMG)
            embed.set_thumbnail(url=config.LOGO)

            log_embed = discord.Embed(
                title="<:ServerSSD:1316165994124804116> | __The server has been shut down, please confirm below!__",
                description=f"> - **Sent By:** <@{interaction.user.id}>\n> - **Time Sent:** {config.current_time()}\n> - **Action Done:** `SSDed`\n"
                            f"\n**__SSD Information:__**\n> - **Reason:** {reason}\n> - **User(s) Requesting:** {user}\n> - **Other Staff In-Game:** {other_staff}\n> - **Used the Staff Request:** {melonly}\n> - **Anything Else:** {anything_else}",
                color=discord.Color.from_str(config.colors.RED)
            )
            log_embed.set_image(
                url=imgs.RED_SESSION_IMG)

            from config import SSU_ID
            channel = self.bot.get_channel(config.channels.SERVER_STATUS)
            msg = await channel.fetch_message(SSU_ID)

            await msg.delete()
            msg = await self.bot.get_channel(config.channels.SERVER_STATUS).send(embed=embed)
            await self.bot.get_channel(config.channels.SESSION_LOGGING).send(content="<@&1354551020956549303", embed=log_embed, view=FinalLogConfirmation(session_type="ssd"))
            await self.interaction.edit_original_response(view=None)
            await interaction.response.send_message(content="Successfully SSDed.", ephemeral=True)
            config.session_status = "ssd"
            config.SSD_ID = msg.id
            # await stop_reminders()

        except Exception as e:
            print("ssd modal error -", e)
            from config import SSU_ID
            print(traceback.print_exc(), SSU_ID)

class SessionsMenu(discord.ui.View):
    def __init__(self, bot, session_status):
        super().__init__()
        self.bot = bot
        self.session_status = session_status

    @discord.ui.select(
        placeholder="Select session type...",
        min_values=1,
        max_values=1,

        options=[
            discord.SelectOption(label="SSU", description="Startup the server!", value="ssu", emoji="<:ServerSSU:1316165992727973948>"),
            discord.SelectOption(label="SSD", description="Shutdown the server!", value="ssd", emoji="<:ServerSSD:1316165994124804116>"),
            discord.SelectOption(label="LPP", description="Send the Low Player Ping Message!", value="lpp", emoji="<:ServerLLP:1316165989012082708>"),
            discord.SelectOption(label="Restart", description="Send the Server Restart Message!", value="restart", emoji="<:ServerRestart:1386846452805931021>"),
            discord.SelectOption(label="Crash", description="Send the Server Crash Message!", value="crash", emoji="<:ServerCrash:1316165991561957447>"),
            discord.SelectOption(label="Update", description="Send the ER:LC Update Message!", value="update", emoji="<:ServerUpdate:1316165989963927645>")
        ]
    )
    async def select_callback(self, interaction: discord.Interaction, select: discord.ui.Select):
        value = select.values[0]

        if value == "ssu" and self.session_status == "ssu":
            await interaction.response.send_message("An SSU is already active!", ephemeral=True)
            return
        elif value == "ssd" and self.session_status == "ssd":
            await interaction.response.send_message("An SSD is already active!", ephemeral=True)
            return
        elif value in ["lpp", "crash", "update", "restart"] and self.session_status == "ssd":
            await interaction.response.send_message(f"I can't do a `{value}` ping during SSD!", ephemeral=True)
            return

        message_value = {
            "ssu": "SSU",
            "ssd": "SSD",
            "llp": "Low Player",
            "restart": "Server Restart",
            "crash": "Server Crash",
            "update": "Server Update"
        }.get(value, value)

        embed = discord.Embed(
            title="Confirmation",
            description=f"Please confirm you would like to send the `{message_value}` message.",
            color=discord.Color.from_str(config.colors.GREY)
        )
        embed.set_footer(
            text="Please note: This action will be logged.",
            icon_url="https://cdn.discordapp.com/attachments/1354553136655892500/1387121295673524255/download.png"
        )

        await interaction.response.send_message(embed=embed, ephemeral=True, view=SessionConfirmationView(self.bot, session_type=value))
