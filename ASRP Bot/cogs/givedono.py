import discord.ext, datetime
from config import SUPPORTERS_CHANNEL, SUPPORTERS_LOGGING_CHANNEL


class GiveDonoCog(discord.ext.commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name="givedono", description="Send the Donator message within #𝐒upporters!")
    @discord.app_commands.describe(user="The user who bought the donation", donation="The type of donation")
    @discord.app_commands.choices(donation=
                                  [
                                      discord.app_commands.Choice(name="Silver Donator", value="silver"),
                                      discord.app_commands.Choice(name="Gold Donator", value="gold"),
                                      discord.app_commands.Choice(name="Platinum Donator", value="platinum")
                                   ])
    async def get_user_id(self, interaction: discord.Interaction, user: discord.User, donation: str):
        print(f"{interaction.user.name} - <@{interaction.user.id}> - Used the dono command")
        if donation == "silver":
            embed = discord.Embed(
                title="<:SilverDonator:1182891513659789384> | __New Silver Donator!__",
                description=f"> - Thank you so much to {user.mention} for purchasing **[Silver Donator!](https://www.roblox.com/catalog/15581788402/Silver-Donator)**\n> - Want to support ASRP? Check our our https://discord.com/channels/1182487341386969158/1182828152259608598!",
                color=discord.Color.from_str("#a7a8a7"),
                url="https://discord.com/channels/1182487341386969158/1182828152259608598"
            )
            embed.set_footer(text="ASRP - Donator Messages", icon_url="https://images-ext-1.discordapp.net/external/8p-nHvCtd_rNRujsHOy_OzFx0OsJyefSJ0lGurVTVCs/%3Fformat%3Dwebp%26quality%3Dlossless/https/images-ext-1.discordapp.net/external/khwBIopKG3PFjZErVP6n4yWRp15Om2i5MNvIkeeVDWY/%253Fv%253D1/https/cdn.discordapp.com/emojis/1182891513659789384.png")
            embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/khwBIopKG3PFjZErVP6n4yWRp15Om2i5MNvIkeeVDWY/%3Fv%3D1/https/cdn.discordapp.com/emojis/1182891513659789384.png?format=webp&quality=lossless")

            log_embed = discord.Embed(
                title="<:SilverDonator:1182891513659789384> | __Someone has been given Silver Donator!__",
                description=f"""
> - **Given By:** {interaction.user.mention}
> - **Given To:** {user.mention}
> - **Time Given**: <t:{int(datetime.datetime.now().timestamp())}:R>""",
                color=discord.Color.from_str("#a7a8a7")
            )
            log_embed.set_footer(text="ASRP - Donator Logging", icon_url="https://images-ext-1.discordapp.net/external/8p-nHvCtd_rNRujsHOy_OzFx0OsJyefSJ0lGurVTVCs/%3Fformat%3Dwebp%26quality%3Dlossless/https/images-ext-1.discordapp.net/external/khwBIopKG3PFjZErVP6n4yWRp15Om2i5MNvIkeeVDWY/%253Fv%253D1/https/cdn.discordapp.com/emojis/1182891513659789384.png")
            log_embed.set_thumbnail(
                url="https://images-ext-1.discordapp.net/external/khwBIopKG3PFjZErVP6n4yWRp15Om2i5MNvIkeeVDWY/%3Fv%3D1/https/cdn.discordapp.com/emojis/1182891513659789384.png?format=webp&quality=lossless")

            await user.add_roles(self.bot.get_guild(1182487341386969158).get_role(1182827823598153788))

        elif donation == "gold":
            embed = discord.Embed(
                title="<:GoldDonator:1182891511009005628> | __New Gold Donator!__",
                description=f"> - Thank you so much to {user.mention} for purchasing **[Gold Donator!](https://www.roblox.com/catalog/15581795355/Gold-Donator)**\n> - Want to support ASRP? Check our our https://discord.com/channels/1182487341386969158/1182828152259608598!",
                color=discord.Color.from_str("#d5c515"),
                url="https://discord.com/channels/1182487341386969158/1182828152259608598"
            )
            embed.set_footer(text="ASRP - Donator Messages",
                             icon_url="https://images-ext-1.discordapp.net/external/VG-lQ2PET0pmR5fo4eyRtUEbRxsMu9bb_WAK7LxBNr0/%3Fformat%3Dwebp%26quality%3Dlossless/https/images-ext-1.discordapp.net/external/-ns7-XAvApX0iIrPkzQo0xuXr7fU1TCMUzmxn0xZaEA/%253Fv%253D1/https/cdn.discordapp.com/emojis/1182891511009005628.png")
            embed.set_thumbnail(
                url="https://images-ext-1.discordapp.net/external/-ns7-XAvApX0iIrPkzQo0xuXr7fU1TCMUzmxn0xZaEA/%3Fv%3D1/https/cdn.discordapp.com/emojis/1182891511009005628.png?format=webp&quality=lossless")

            log_embed = discord.Embed(
                title="<:GoldDonator:1182891511009005628> | __Someone has been given Gold Donator!__",
                description=f"""
    > - **Given By:** {interaction.user.mention}
    > - **Given To:** {user.mention}
    > - **Time Given**: <t:{int(datetime.datetime.now().timestamp())}:R>""",
                color=discord.Color.from_str("#d5c515")
            )
            log_embed.set_footer(text="ASRP - Donator Logging",
                             icon_url="https://images-ext-1.discordapp.net/external/VG-lQ2PET0pmR5fo4eyRtUEbRxsMu9bb_WAK7LxBNr0/%3Fformat%3Dwebp%26quality%3Dlossless/https/images-ext-1.discordapp.net/external/-ns7-XAvApX0iIrPkzQo0xuXr7fU1TCMUzmxn0xZaEA/%253Fv%253D1/https/cdn.discordapp.com/emojis/1182891511009005628.png")
            log_embed.set_thumbnail(
                url="https://images-ext-1.discordapp.net/external/-ns7-XAvApX0iIrPkzQo0xuXr7fU1TCMUzmxn0xZaEA/%3Fv%3D1/https/cdn.discordapp.com/emojis/1182891511009005628.png?format=webp&quality=lossless")

            await user.add_roles(self.bot.get_guild(1182487341386969158).get_role(1182827822776074393))

        elif donation == "platinum":
            embed = discord.Embed(
                title="<:PlatinumDonator:1182891507263483954> | __New Platinum Donator!__",
                description=f"> - Thank you so much to {user.mention} for purchasing **[Platinum Donator!](https://www.roblox.com/catalog/15581798820/Platinum-Donator)**\n> - Want to support ASRP? Check our our https://discord.com/channels/1182487341386969158/1182828152259608598!",
                color=discord.Color.from_str("#353533"),
                url="https://discord.com/channels/1182487341386969158/1182828152259608598"
            )
            embed.set_footer(text="ASRP - Donator Messages",
                             icon_url="https://images-ext-1.discordapp.net/external/65t7-NHgHxCCow49Laao-fOlKPQA_b8aIDQCZBku6Pg/%3Fformat%3Dwebp%26quality%3Dlossless/https/images-ext-1.discordapp.net/external/fYJnc2Q0wFKL7MG5pPYlJby2tTSzDVsyqiN2YAhBPPE/%253Fv%253D1/https/cdn.discordapp.com/emojis/1182891507263483954.png")
            embed.set_thumbnail(
                url="https://images-ext-1.discordapp.net/external/fYJnc2Q0wFKL7MG5pPYlJby2tTSzDVsyqiN2YAhBPPE/%3Fv%3D1/https/cdn.discordapp.com/emojis/1182891507263483954.png?format=webp&quality=lossless")

            log_embed = discord.Embed(
                title="<:GoldDonator:1182891511009005628> | __Someone has been given Gold Donator!__",
                description=f"""
    > - **Given By:** {interaction.user.mention}
    > - **Given To:** {user.mention}
    > - **Time Given**: <t:{int(datetime.datetime.now().timestamp())}:R>""",
                color=discord.Color.from_str("#353533")
            )
            log_embed.set_footer(text="ASRP - Donator Logging",
                             icon_url="https://images-ext-1.discordapp.net/external/65t7-NHgHxCCow49Laao-fOlKPQA_b8aIDQCZBku6Pg/%3Fformat%3Dwebp%26quality%3Dlossless/https/images-ext-1.discordapp.net/external/fYJnc2Q0wFKL7MG5pPYlJby2tTSzDVsyqiN2YAhBPPE/%253Fv%253D1/https/cdn.discordapp.com/emojis/1182891507263483954.png")
            log_embed.set_thumbnail(
                url="https://images-ext-1.discordapp.net/external/fYJnc2Q0wFKL7MG5pPYlJby2tTSzDVsyqiN2YAhBPPE/%3Fv%3D1/https/cdn.discordapp.com/emojis/1182891507263483954.png?format=webp&quality=lossless")

            await user.add_roles(self.bot.get_guild(1182487341386969158).get_role(1182827821886885908))


        await self.bot.get_channel(SUPPORTERS_CHANNEL).send(embed=embed)
        await self.bot.get_channel(SUPPORTERS_LOGGING_CHANNEL).send(embed=log_embed)
        await interaction.response.send_message(f"Successfully sent the {donation} donator message for {user.mention}.", ephemeral=True)


async def setup(bot):
    await bot.add_cog(GiveDonoCog(bot))
