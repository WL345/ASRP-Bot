import discord
from discord.ext import commands
from apscheduler.schedulers.background import BackgroundScheduler
import asyncio

TOKEN = "MTM4NjgwMzA2NzMzNjUyMzgyNw.GN9sRG.Hobwkk-DXfYtAuER00gxO3KUOyV5YF9SbqDs10"

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="a!", intents=intents)

scheduler = BackgroundScheduler()
scheduler.start()


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Commands synced - {len(synced)}\n")
        for cmd in synced:
            print(f"</{cmd.name}:{cmd.id}>")
    except Exception as e:
        print(f"Error syncing commands: {e}")


async def load_extensions():
    await bot.load_extension("cogs.sessions")
    await bot.load_extension("cogs.say")
    await bot.load_extension("cogs.test")

async def main():
    async with bot:
        await load_extensions()
        await bot.start(TOKEN)


import nest_asyncio
nest_asyncio.apply()

asyncio.run(main())
