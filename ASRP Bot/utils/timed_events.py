import asyncio, discord, config


class ReminderManager:
    def __init__(self, bot: discord.Client):
        self.bot = bot
        self._task: asyncio.Task | None = None

    def start(self):
        if self._task is None or self._task.done():
            self._task = asyncio.create_task(self._reminder_loop())

    async def stop(self):
        if self._task and not self._task.done():
            self._task.cancel()
            try:
                await self._task
            except asyncio.CancelledError:
                pass
        self._task = None

    async def _reminder_loop(self):
        try:
            embed = discord.Embed(
                title="<:ASRP:1182842789780799539> | Staffing Reminders!",
                color=discord.Color.from_str(config.colors.LIGHT_BLUE)
            )

            embed.add_field(name="__Discord Check Reminder__",
                            value="> - Hello Online Staff! If you are Staffing and aren't stacked on calls or there are multiple of you on, You should be doing Discord Checks for people who aren't in our Discord server and getting them in! If there are multiple of you, how you guys split this up is completely up to you!", inline=False)
            embed.add_field(name="__TM Supervising Reminder__",
                            value="> - Hello Online Staff! If you have the <@&1182827710855254056> role, there are 30+ players in-game, and the server does not have 3+ active modcalls, please ensure you are SVing a Trial Moderator or have pinged the <@&1182827713392820294> role and no one asked for a Supervision from you.", inline=False)
            embed.add_field(name="__Booster Check Reminder__",
                            value="> - Hello Online staffStaff! If you aren't stacked on calls, please make check users for any booster vehicles using the Melonly Panel! To see which vehicles are limited to boosters, see [this](https://docs.google.com/spreadsheets/d/1Ry3jTRd5S1IEkl-kuFuF_BXSwqfVdtMTmyD4a-vhCZs/edit?gid=7252186#gid=7252186) document!",
                            inline=False)

            embed.set_footer(text="Alaska State Roleplay - Staffing Reminders",
                             icon_url="https://media.discordapp.net/attachments/1182828263828103240/1183816241241133147/ASRP_Staff.png?ex=686d4f4a&is=686bfdca&hm=68e8bfe78675733a1c4b52e449f92f5d33b482f5bda3362a9c5af5151918affc&")
            embed.set_image(url=config.imgs.LIGHT_BLUE_IMG),
            embed.set_thumbnail(
                url="https://media.discordapp.net/attachments/1182828263828103240/1183816241241133147/ASRP_Staff.png?ex=686d4f4a&is=686bfdca&hm=68e8bfe78675733a1c4b52e449f92f5d33b482f5bda3362a9c5af5151918affc&")

            log_embed = discord.Embed(
                title="Automated Message Sent!",
                description=f"""
                > - **Message Sent:** Discord/SV Reminder
                > - **Time Sent:** {config.current_time()}""",
                color=discord.Color.from_str(config.colors.LIGHT_BLUE)
            )
            log_embed.set_image(url=config.imgs.LIGHT_BLUE_IMG)
            log_embed.set_thumbnail(url=config.LOGO)
            log_embed.set_footer(text="ASRP - Automated Command Logging System", icon_url=config.LOGO)


            while True:
                try:
                    view = discord.ui.View()
                    view.add_item(discord.ui.Button(label="Mark as Complete", style=discord.ButtonStyle.green, custom_id="dc_reminder"))
                    await self.bot.get_channel(1354553136655892500).send("<@&1182827685420994680>", embed=embed, view=view)
                    await self.bot.get_channel(config.channels.AUTOMATED_MESSAGES_LOGGING).send(embed=log_embed)

                except Exception as e:
                    print(f"Reminder send failed: {e}")

                await asyncio.sleep(60)

        except asyncio.CancelledError:
            return
        except Exception as e:
            print(f"Reminder loop crashed: {e}")


reminder_manager: ReminderManager | None = None

def initialize_reminders(bot: discord.Client):
    global reminder_manager
    if reminder_manager is None:
        reminder_manager = ReminderManager(bot)

def start_reminders():
    reminder_manager.start()

async def stop_reminders():
    await reminder_manager.stop()
