# import asyncio
# import discord
#
#
# class ReminderManager:
#     def __init__(self, bot: discord.Client):
#         self.bot = bot
#         self._task: asyncio.Task | None = None
#
#     def start(self):
#         if self._task is None or self._task.done():
#             self._task = asyncio.create_task(self._reminder_loop())
#
#     async def stop(self):
#         if self._task and not self._task.done():
#             self._task.cancel()
#             try:
#                 await self._task
#             except asyncio.CancelledError:
#                 pass
#         self._task = None
#
#     async def _reminder_loop(self):
#         try:
#             while True:
#
#                 try:
#                     embed = discord.Embed(
#                         title="Session Reminder",
#                         description="ykyuh",
#                         color=discord.Color.green()
#                     )
#                     view = discord.ui.View()
#                     channel = self.bot.get_channel(1354553136655892500)
#                     if channel:
#                         await channel.send(embed=embed, view=view)
#                     else:
#                         print("ReminderManager: Channel not found.")
#
#                 except Exception as e:
#                     print(f"Reminder send failed: {e}")
#
#                 await asyncio.sleep(10)
#
#         except asyncio.CancelledError:
#             return
#         except Exception as e:
#             print(f"Reminder loop crashed: {e}")
#
#
# reminder_manager: ReminderManager | None = None
#
# def initialize(bot: discord.Client):
#     global reminder_manager
#     if reminder_manager is None:
#         reminder_manager = ReminderManager(bot)
#
# def start_reminders():
#     reminder_manager.start()
#
# async def stop_reminders():
#     await reminder_manager.stop()
