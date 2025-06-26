import discord
import datetime
from utils.colors import colors
from config import *
import config


class FinalLogConfirmation(discord.ui.View):
    def __init__(self, session_type):
        super().__init__()
        self.session_type = session_type

    @discord.ui.button(label="Confirm", style=discord.ButtonStyle.green)
    async def confirm_log(self, interaction: discord.Interaction, button: discord.ui.Button):

        original_embed = interaction.message.embeds[0]
        original_content = original_embed.description
        if self.session_type == "ssu":
            original_content = original_content.replace("**Action Done:** `SSUed`\n", f"**Action Done:** `SSUed`\n> - **Time Confirmed:** <t:{int(datetime.datetime.now().timestamp())}:R>\n")

            edited_embed = discord.Embed(
                description=original_content,
                title="__<:ServerSSU:1316165992727973948> | The server startup message has been confirmed!__",
                color=discord.Color.from_str(colors.GREEN)
            )
            edited_embed.set_footer(text=f"Confirmed by: {interaction.user.nick}", icon_url=interaction.user.avatar)
            edited_embed.set_image(url=GREEN_SESSION_IMG)

        elif self.session_type == "ssd":
            original_content = original_content.replace("**Action Done:** `SSDed`\n", f"**Action Done:** `SSDed`\n> - **Time Confirmed:** <t:{int(datetime.datetime.now().timestamp())}:R>\n")

            edited_embed = discord.Embed(
                description=original_content,
                title="__<:ServerSSD:1316165994124804116> | The server shutdown message has been confirmed!__",
                color=discord.Color.from_str(colors.RED)
            )
            edited_embed.set_footer(text=f"Confirmed by: {interaction.user.nick}", icon_url=interaction.user.avatar)
            edited_embed.set_image(url=RED_SESSION_IMG)

        elif self.session_type == "lpp":
            original_content = f"{original_content}\n> - **Time Confirmed:** <t:{int(datetime.datetime.now().timestamp())}:R>"

            edited_embed = discord.Embed(
                description=original_content,
                title="__<:ServerLLP:1316165989012082708> | The Low Player Ping message has been confirmed!__",
                color=discord.Color.from_str(colors.YELLOW)
            )
            edited_embed.set_footer(text=f"Confirmed by: {interaction.user.nick}", icon_url=interaction.user.avatar)
            edited_embed.set_image(url=YELLOW_SESSION_IMG)

        elif self.session_type == "restart":
            original_content = f"{original_content}\n> - **Time Confirmed:** <t:{int(datetime.datetime.now().timestamp())}:R>"

            edited_embed = discord.Embed(
                description=original_content,
                title="__<:ServerRestart:1386846452805931021> | The Server Restart message has been confirmed!__",
                color=discord.Color.from_str(colors.ORANGE)
            )
            edited_embed.set_footer(text=f"Confirmed by: {interaction.user.nick}", icon_url=interaction.user.avatar)
            edited_embed.set_image(url=ORANGE_SESSION_IMG)

        elif self.session_type == "crash":
            original_content = f"{original_content}\n> - **Time Confirmed:** <t:{int(datetime.datetime.now().timestamp())}:R>"

            edited_embed = discord.Embed(
                description=original_content,
                title="__<:ServerCrash:1316165991561957447> | The Server Crash message has been confirmed!__",
                color=discord.Color.from_str(colors.GREY)
            )
            edited_embed.set_footer(text=f"Confirmed by: {interaction.user.nick}", icon_url=interaction.user.avatar)
            edited_embed.set_image(url=GREY_SESSION_IMG)

        elif self.session_type == "update":
            original_content = f"{original_content}\n> - **Time Confirmed:** <t:{int(datetime.datetime.now().timestamp())}:R>"

            edited_embed = discord.Embed(
                description=original_content,
                title="__<:ServerUpdate:1316165989963927645> | The Server Update message has been confirmed!__",
                color=discord.Color.from_str(colors.BLUE)
            )
            edited_embed.set_footer(text=f"Confirmed by: {interaction.user.nick}", icon_url=interaction.user.avatar)
            edited_embed.set_image(url=BLUE_SESSION_IMG)

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
        elif self.session_type == "ssd":
            await interaction.response.send_modal(SSDModal(self.bot, interaction))

        elif self.session_type == "lpp":
            try:
                embed = discord.Embed(
                    title="__<:ServerLLP:1316165989012082708> | Low Player Ping!__",
                    description=f"""
                        > - Our in-game server is currently low on players! Join the server with code **[ALASKA](https://policeroleplay.community/join?code=ALASKA&placeId=2534724415)** and engage in some great roleplays!""",
                    color=discord.Color.from_str(colors.YELLOW)
                )
                embed.set_image(url=YELLOW_SESSION_IMG)
                embed.set_footer(text="This message will be deleted in 30 minutes.",
                                 icon_url="https://media.discordapp.net/attachments/1182828263828103240/1183834014465925130/file-z2wbRRQ45BNH3lmnqqBb4L3M_1.png?ex=685c3c57&is=685aead7&hm=0e89fd025b1cddfef0950fb6665035e56fd576481c18d5034ea3d9d9cca1f922&")
                embed.set_thumbnail(
                    url="https://media.discordapp.net/attachments/1182828263828103240/1183834014465925130/file-z2wbRRQ45BNH3lmnqqBb4L3M_1.png?ex=685c3c57&is=685aead7&hm=0e89fd025b1cddfef0950fb6665035e56fd576481c18d5034ea3d9d9cca1f922&format=webp&quality=lossless&width=810&height=810&")

                await self.bot.get_channel(SERVER_STATUS_CHANNEL).send("@her e <@&1182908708821401631",
                                                                       embed=embed, delete_after=1800)

                log_embed = discord.Embed(
                    title="<:ServerLLP:1316165989012082708> | __The Low Player Ping has been sent, please confirm below!__",
                    description=f"> - **Sent By:** <@{interaction.user.id}>\n> - **Time Sent:** <t:{int(datetime.datetime.now().timestamp())}:R>\n> - **Action Done:** `LLP`",
                    color=discord.Color.from_str(colors.YELLOW)
                )
                log_embed.set_image(
                    url=YELLOW_SESSION_IMG)

                await self.bot.get_channel(SESSION_LOGGING_CHANNEL).send(
                    content="<@&1354551020956549303",
                    embed=log_embed,
                    view=FinalLogConfirmation(session_type="lpp")
                )

                await interaction.response.edit_message(content="Successfully sent the LPP message.", view=None,
                                                        embed=None)

            except Exception as e:
                print(f"llp sending error - {e}")

        elif self.session_type == "restart":
            try:
                embed = discord.Embed(
                    title="__<:ServerRestart:1386846452805931021> | Server Restart!__",
                    description=f"> - We have **restarted** our in-game server, either due to mass amounts of lag, trollers, or another reason. Feel free to rejoin with the code: **[ALASKA](https://policeroleplay.community/join?code=ALASKA&placeId=2534724415)**!",
                    color=discord.Color.from_str(colors.ORANGE)
                )
                embed.set_image(url=ORANGE_SESSION_IMG)
                embed.set_footer(text="This message will be deleted in 30 minutes.",
                                 icon_url="https://media.discordapp.net/attachments/1182828263828103240/1183834014465925130/file-z2wbRRQ45BNH3lmnqqBb4L3M_1.png?ex=685c3c57&is=685aead7&hm=0e89fd025b1cddfef0950fb6665035e56fd576481c18d5034ea3d9d9cca1f922&")
                embed.set_thumbnail(
                    url="https://media.discordapp.net/attachments/1182828263828103240/1183834014465925130/file-z2wbRRQ45BNH3lmnqqBb4L3M_1.png?ex=685c3c57&is=685aead7&hm=0e89fd025b1cddfef0950fb6665035e56fd576481c18d5034ea3d9d9cca1f922&format=webp&quality=lossless&width=810&height=810&")

                await self.bot.get_channel(SERVER_STATUS_CHANNEL).send("@her e", embed=embed, delete_after=1800)

                log_embed = discord.Embed(
                    title="<:ServerRestart:1386846452805931021> | __The Server Restart message has been sent, please confirm below!__",
                    description=f"> - **Sent By:** <@{interaction.user.id}>\n> - **Time Sent:** <t:{int(datetime.datetime.now().timestamp())}:R>\n> - **Action Done:** `Restart`",
                    color=discord.Color.from_str(colors.ORANGE)
                )
                log_embed.set_image(
                    url=ORANGE_SESSION_IMG)

                await self.bot.get_channel(SESSION_LOGGING_CHANNEL).send(
                    content="<@&1354551020956549303",
                    embed=log_embed,
                    view=FinalLogConfirmation(session_type="restart")
                )

                await interaction.response.edit_message(content="Successfully sent the restart message.",
                                                        view=None, embed=None)

            except Exception as e:
                print(f"restart sending error - {e}")

        elif self.session_type == "crash":
            try:
                embed = discord.Embed(
                    title="__<:ServerCrash:1316165991561957447> | Server Crash!__",
                    description=f"> - Our in-game server has **crashed**! Feel free to rejoin with the code: **[ALASKA](https://policeroleplay.community/join?code=ALASKA&placeId=2534724415)**. We apologize for the inconvenience!",
                    color=discord.Color.from_str(colors.GREY)
                )
                embed.set_image(url=GREY_SESSION_IMG)
                embed.set_footer(text="This message will be deleted in 30 minutes.",
                                 icon_url="https://media.discordapp.net/attachments/1182828263828103240/1183834014465925130/file-z2wbRRQ45BNH3lmnqqBb4L3M_1.png?ex=685c3c57&is=685aead7&hm=0e89fd025b1cddfef0950fb6665035e56fd576481c18d5034ea3d9d9cca1f922&")
                embed.set_thumbnail(
                    url="https://media.discordapp.net/attachments/1182828263828103240/1183834014465925130/file-z2wbRRQ45BNH3lmnqqBb4L3M_1.png?ex=685c3c57&is=685aead7&hm=0e89fd025b1cddfef0950fb6665035e56fd576481c18d5034ea3d9d9cca1f922&format=webp&quality=lossless&width=810&height=810&")

                await self.bot.get_channel(SERVER_STATUS_CHANNEL).send("@her e", embed=embed, delete_after=1800)

                log_embed = discord.Embed(
                    title="<:ServerCrash:1316165991561957447>> | __The Server Crash message has been sent, please confirm below!__",
                    description=f"> - **Sent By:** <@{interaction.user.id}>\n> - **Time Sent:** <t:{int(datetime.datetime.now().timestamp())}:R>\n> - **Action Done:** `Crash`",
                    color=discord.Color.from_str(colors.GREY)
                )
                log_embed.set_image(
                    url=GREY_SESSION_IMG)

                await self.bot.get_channel(SESSION_LOGGING_CHANNEL).send(
                    content="<@&1354551020956549303",
                    embed=log_embed,
                    view=FinalLogConfirmation(session_type="crash")
                )

                await interaction.response.edit_message(content="Successfully sent the server crash message.",
                                                        view=None,
                                                        embed=None)

            except Exception as e:
                print(f"crash sending error - {e}")

        elif self.session_type == "update":
            try:
                embed = discord.Embed(
                    title="__<:ServerUpdate:1316165989963927645> | PRC Update!__",
                    description=f"> - Our host game, ER:LC (Emergency Response: Liberty County) has **updated**! Feel free to join back and enjoy the new content with our code: **[ALASKA](https://policeroleplay.community/join?code=ALASKA&placeId=2534724415)**!",
                    color=discord.Color.from_str(colors.BLUE)
                )
                embed.set_image(url=BLUE_SESSION_IMG)
                embed.set_footer(text="This message will be deleted in 30 minutes.",
                                 icon_url="https://media.discordapp.net/attachments/1182828263828103240/1183834014465925130/file-z2wbRRQ45BNH3lmnqqBb4L3M_1.png?ex=685c3c57&is=685aead7&hm=0e89fd025b1cddfef0950fb6665035e56fd576481c18d5034ea3d9d9cca1f922&")
                embed.set_thumbnail(
                    url="https://media.discordapp.net/attachments/1182828263828103240/1183834014465925130/file-z2wbRRQ45BNH3lmnqqBb4L3M_1.png?ex=685c3c57&is=685aead7&hm=0e89fd025b1cddfef0950fb6665035e56fd576481c18d5034ea3d9d9cca1f922&format=webp&quality=lossless&width=810&height=810&")

                await self.bot.get_channel(SERVER_STATUS_CHANNEL).send("@her e", embed=embed, delete_after=1800)

                log_embed = discord.Embed(
                    title="<:ServerUpdate:1316165989963927645> | __The Server Update message has been sent, please confirm below!__",
                    description=f"> - **Sent By:** <@{interaction.user.id}>\n> - **Time Sent:** <t:{int(datetime.datetime.now().timestamp())}:R>\n> - **Action Done:** `Update`",
                    color=discord.Color.from_str(colors.BLUE)
                )
                log_embed.set_image(
                    url=BLUE_SESSION_IMG)

                await self.bot.get_channel(SESSION_LOGGING_CHANNEL).send(
                    content="<@&1354551020956549303",
                    embed=log_embed,
                    view=FinalLogConfirmation(session_type="update")
                )

                await interaction.response.edit_message(content="Successfully sent the server update message.",
                                                        view=None, embed=None)

            except Exception as e:
                print(f"update sending error - {e}")

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
        > - **Server Code:** [ALASKA](https://policeroleplay.community/join?code=ALASKA&placeId=2534724415)  
        > - **Started By:** <@{interaction.user.id}>
        
        > This session has been open since <t:{int(datetime.datetime.now().timestamp())}:R>
        """,
                color=discord.Color.from_str(colors.GREEN)
            )
            embed.set_image(
                url=GREEN_SESSION_IMG)
            embed.set_thumbnail(
                url="https://media.discordapp.net/attachments/1182828263828103240/1183834014465925130/file-z2wbRRQ45BNH3lmnqqBb4L3M_1.png")
            embed.set_footer(
                text="Have any questions? Make a support ticket!",
                icon_url="https://media.discordapp.net/attachments/1182828263828103240/1183834014465925130/file-z2wbRRQ45BNH3lmnqqBb4L3M_1.png"
            )

            await self.bot.get_channel(SERVER_STATUS_CHANNEL).send("<@&1182908708821401631", embed=embed)

            log_embed = discord.Embed(
                title="<:ServerSSU:1316165992727973948> | __The server has been started, please confirm below!__",
                description=f"> - **Sent By:** <@{interaction.user.id}>\n> - **Time Sent:** <t:{int(datetime.datetime.now().timestamp())}:R>\n> - **Action Done:** `SSUed`\n"
                            f"\n**__SSUer(s):__**\n> - {user1}\n> - {user2}",
                color=discord.Color.from_str(colors.GREEN)
            )
            log_embed.set_image(
                url=GREEN_SESSION_IMG)

            await self.bot.get_channel(SESSION_LOGGING_CHANNEL).send(
                content="<@&1354551020956549303",
                embed=log_embed,
                view=FinalLogConfirmation("ssu")
            )

            config.session_status = "ssu"

            # await self.interaction.edit_original_response(content="Successfully SSUed! Please check https://discord.com/channels/1182487341386969158/1187789091459305512 and complete any requests made.", embed=None, view=None)
            await self.interaction.edit_original_response(view=None)
            await interaction.response.send_message(
                content="Successfully SSUed! Please check https://discord.com/channels/1182487341386969158/1187789091459305512 and complete any requests made.",
                ephemeral=True
            )


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
    
                    > This session shutdown <t:{int(datetime.datetime.now().timestamp())}:R>.
                    """,
                color=discord.Color.from_str(colors.RED)
        )
            embed.set_footer(text="Have any questions? Make a support ticket!", icon_url="https://media.discordapp.net/attachments/1182828263828103240/1183834014465925130/file-z2wbRRQ45BNH3lmnqqBb4L3M_1.png?ex=685c3c57&is=685aead7&hm=0e89fd025b1cddfef0950fb6665035e56fd576481c18d5034ea3d9d9cca1f922&")
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/1182828263828103240/1183834014465925130/file-z2wbRRQ45BNH3lmnqqBb4L3M_1.png?ex=685c3c57&is=685aead7&hm=0e89fd025b1cddfef0950fb6665035e56fd576481c18d5034ea3d9d9cca1f922&format=webp&quality=lossless&width=810&height=810&")

            await self.bot.get_channel(SERVER_STATUS_CHANNEL).send(embed=embed)

            log_embed = discord.Embed(
                title="<:ServerSSD:1316165994124804116> | __The server has been shut down, please confirm below!__",
                description=f"> - **Sent By:** <@{interaction.user.id}>\n> - **Time Sent:** <t:{int(datetime.datetime.now().timestamp())}:R>\n> - **Action Done:** `SSDed`\n"
                            f"\n**__SSD Information:__**\n> - **Reason:** {reason}\n> - **User(s) Requesting:** {user}\n> - **Other Staff In-Game:** {other_staff}\n> - **Used the Staff Request:** {melonly}\n> - **Anything Else:** {anything_else}",
                color=discord.Color.from_str(colors.RED)
            )
            log_embed.set_image(
                url=RED_SESSION_IMG)

            await self.bot.get_channel(SESSION_LOGGING_CHANNEL).send(
                content="<@&1354551020956549303",
                embed=log_embed,
                view=FinalLogConfirmation(session_type="ssd")
            )

            config.session_status = "ssd"

            await self.interaction.edit_original_response(view=None)
            await interaction.response.send_message(
                content="Successfully SSDed.",
                ephemeral=True
            )

        except Exception as e:
            print("ssd modal error -", e)


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
            discord.SelectOption(label="Session Start Up", value="ssu", emoji="<:ServerSSU:1316165992727973948>"),
            discord.SelectOption(label="Session Shut Down", value="ssd", emoji="<:ServerSSD:1316165994124804116>"),
            discord.SelectOption(label="Low Player Ping", value="lpp", emoji="<:ServerLLP:1316165989012082708>"),
            discord.SelectOption(label="Session Restart", value="restart", emoji="<:ServerRestart:1386846452805931021>"),
            discord.SelectOption(label="Session Crash", value="crash", emoji="<:ServerCrash:1316165991561957447>"),
            discord.SelectOption(label="PRC Update", value="update", emoji="<:ServerUpdate:1316165989963927645>")
        ]
    )
    async def select_callback(self, interaction: discord.Interaction, select: discord.ui.Select):
        value = select.values[0]

        print(value, self.session_status)

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
            color=discord.Color.from_str(colors.GREY)
        )
        embed.set_footer(
            text="Please note: This action will be logged.",
            icon_url="https://cdn.discordapp.com/attachments/1354553136655892500/1387121295673524255/download.png"
        )

        await interaction.response.send_message(embed=embed, ephemeral=True, view=SessionConfirmationView(self.bot, session_type=value))
