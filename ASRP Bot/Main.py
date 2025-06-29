import discord
from discord.ext import commands
import asyncio

TOKEN = "MTM4NjgwMzA2NzMzNjUyMzgyNw.GN9sRG.Hobwkk-DXfYtAuER00gxO3KUOyV5YF9SbqDs10"

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="iykurediytnokwderxiuyerwdxiyu", intents=intents)


@bot.event
async def on_ready():
    # async for msg in bot.get_channel(1182828263828103240).history(limit=100):  # 1387845894182797555 - thread    ####   1387913096680706158 - astro ticket    ####   1182828263828103240 - mgmt chat
    #     print(msg.author, "-", msg.content)
    #     if msg.content == "thanks to juno":
    #         break

    # await bot.tree.sync(guild=bot.get_guild(1182487341386969158))

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
    await bot.load_extension("cogs.dm")
    await bot.load_extension("cogs.id")
    await bot.load_extension("cogs.trustvip")
    await bot.load_extension("cogs.givedono")
    await bot.load_extension("cogs.feedback")
    # await bot.load_extension("cogs.cmds.user_info")         # GET SCREENSHOT

    await bot.load_extension("cogs.debug")



async def main():
    async with bot:
        await load_extensions()
        await bot.start(TOKEN)


import nest_asyncio
nest_asyncio.apply()

asyncio.run(main())
