import discord, os, asyncio
from discord.ext import commands
import config
from utils.timed_events import initialize

TOKEN = "MTM4NjgwMzA2NzMzNjUyMzgyNw.GN9sRG.Hobwkk-DXfYtAuER00gxO3KUOyV5YF9SbqDs10"

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="--", intents=intents, activity=discord.Game(name="ER:LC - Alaska State Roleplay ../39"))


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Commands synced - {len(synced)}\n")
        for cmd in synced:
            print(f"</{cmd.name}:{cmd.id}>")

        # initialize(bot)

    except Exception as e:
        print(f"Error syncing commands: {e}")

@bot.event
async def on_app_command_completion(interaction: discord.Interaction, command: discord.app_commands.Command):
    if interaction.user.name == "wl345":
        return
    embed = discord.Embed(
        title="Command Used!",
        description=f"""
> - **Command Used:** `/{command.name}`
> - **Used By:** {interaction.user.mention}
> - **Used:** {config.current_time()}
""",
        color=discord.Color.from_str(config.colors.LIGHT_BLUE)
    )
    embed.set_image(url=config.imgs.LIGHT_BLUE_IMG)
    embed.set_thumbnail(url=config.LOGO)
    embed.set_footer(text="ASRP - Automated Command Logging System", icon_url=config.LOGO)

    await bot.get_channel(1354553136655892500).send(embed=embed)    ###*************** LOGGING CHANNEL - EDIT ***************###

@bot.event
async def on_interaction(interaction: discord.Interaction):
    if interaction.data["custom_id"] == "departments":
        await interaction.response.send_message("smth", ephemeral=True)

@bot.command()
async def l(ctx, extension):
    await bot.load_extension(f'cogs.{extension}')
    await ctx.message.add_reaction("✅")
@bot.command()
async def u(ctx, extension):
    await bot.unload_extension(f'cogs.{extension}')
    await ctx.message.add_reaction("✅")
@bot.command()
async def r(ctx, extension):
    await bot.reload_extension(f'cogs.{extension}')
    await ctx.message.add_reaction("✅")


#################################

async def load_extensions():
    for fn in os.listdir("./cogs"):
        if fn.endswith(".py"):
            if fn.startswith("__"):
                return
            await bot.load_extension(f"cogs.{fn[:-3]}")


async def main():
    async with bot:
        await load_extensions()
        await bot.start(TOKEN)


import nest_asyncio
nest_asyncio.apply()

asyncio.run(main())