import discord.ext.commands, config

trust_color = "#1c9290"
vip_color = "#1bb155"

class TrustVIPCog(discord.ext.commands.Cog):
    def __init__(self, bot):
        self.bot: discord.ext.commands.Bot = bot

    @discord.app_commands.command(name="trustvip", description="Give Trusted or VIP to a given user!")
    @discord.app_commands.describe(user="The user you want to give trusted/VIP", reason="What is the reason for giving them Trusted/VIP?", trustvip="Trusted or VIP?")
    @discord.app_commands.choices(
        trustvip=[
            discord.app_commands.Choice(name="Trusted", value="trusted"),
            discord.app_commands.Choice(name="VIP", value="vip")
        ]
    )
    async def trustvip(self, interaction: discord.Interaction, user: discord.User, reason: str, trustvip: str):
        print(f"\n{interaction.user.name} - <@{interaction.user.id}> - Used the trustVIP command")
        if trustvip == "vip":
            if "Management Team" in interaction.user.roles:

                vip_embed = discord.Embed(
                    title="__Congratulations on VIP!__",
                    description=f"""
> Hello {user.mention}! You have been given VIP, check below for more information!

> - Given by: {interaction.user.mention}
> - Time Given: {config.current_time()}
> - Reasoning: {reason}

> Check out your perks in https://discord.com/channels/1182487341386969158/1182828152259608598 and enjoy!""",
                    color=discord.Color.from_str(vip_color)
)
                vip_embed.set_footer(text="Have any questions? Make a support ticket!", icon_url="https://images-ext-1.discordapp.net/external/XdehOrLs017PR-CUCII9SpdvRdRDo-mOY9Z-4ymZtW0/%3Fv%3D1/https/cdn.discordapp.com/emojis/1303479934991466606.png")
                vip_embed.set_image(url="https://cdn.discordapp.com/attachments/1182828263828103240/1303479711212634174/output-onlinepngtools_4-fotor-bg-remover-2024110517212.png?ex=685fbdd4&is=685e6c54&hm=752ce74936f1d3736aaf9cc459bafa76b27de6376004068c1e86b58ecadcaa43&")
                vip_embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/XdehOrLs017PR-CUCII9SpdvRdRDo-mOY9Z-4ymZtW0/%3Fv%3D1/https/cdn.discordapp.com/emojis/1303479934991466606.png")

                log_embed = discord.Embed(
                    title="__Someone has been given VIP!__",
                    description=f"""
                > - **Given By:** {interaction.user.mention}
                > - **Given to:** {user.mention}
                > - **Time Given:** {config.current_time()}
                > - **Reasoning:** {reason}""",
                    color=discord.Color.from_str(vip_color)
                )

                log_embed.set_image(url="https://cdn.discordapp.com/attachments/1182828263828103240/1303479711212634174/output-onlinepngtools_4-fotor-bg-remover-2024110517212.png?ex=68606694&is=685f1514&hm=99f879a5bb814f2582aaf5d9ff0ca5040418cc586b59c2b0d9569bea2ac7418a&")
                log_embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/1303479934991466606.png?v=1")
                log_embed.set_footer(icon_url="https://images-ext-1.discordapp.net/external/XdehOrLs017PR-CUCII9SpdvRdRDo-mOY9Z-4ymZtW0/%3Fv%3D1/https/cdn.discordapp.com/emojis/1303479934991466606.png", text="ASRP - /trustvip command logs.")

                try:
                    await user.add_roles(self.bot.get_guild(1182487341386969158).get_role(1182827825359753308))
                    await user.send(embed=vip_embed)
                    await self.bot.get_channel(config.channels.TRUSTED_VIP_LOGGING).send(embed=log_embed)

                    await interaction.response.send_message("Success!", ephemeral=True)
                except Exception as e:
                    print(e)

            else:
                await interaction.response.send_message("You do not have the proper permissions to give VIP!", ephemeral=True)

        elif trustvip == "trusted":

            trusted_embed = discord.Embed(
                title="__Congratulations on Trusted Player!__",
                description=f"""
> Helo {user.mention}! You have been given Trusted Player, check below for more information!

> - Given By: {interaction.user.mention}
> - Time Given: {config.current_time()}
> - Reasoning: {reason}

> Check out your perks in https://discord.com/channels/1182487341386969158/1182828152259608598 and enjoy!""",
                    color=discord.Color.from_str(trust_color)
)

            trusted_embed.set_footer(text="Have any questions? Make a support ticket!", icon_url="https://media.discordapp.net/attachments/1182828263828103240/1345232691422957679/8f959dbeba52b3cd676f35e92b1489e7.png?ex=685f5e12&is=685e0c92&hm=bb51a0dc0c0e3b70b2b0cbf04fc950015d3c7f8c2641a24597e5584219fcea1c&")
            trusted_embed.set_image(url="https://cdn.discordapp.com/attachments/1182828263828103240/1303479711552503868/output-onlinepngtools_4-fotor-bg-remover-2024110517147.png?ex=685fbdd4&is=685e6c54&hm=077d7c61ad03d0d8af584ad7789feee2e01fd13ff44d974af85ba9a1485effaa&")
            trusted_embed.set_thumbnail(url="https://media.discordapp.net/attachments/1182828263828103240/1345232691422957679/8f959dbeba52b3cd676f35e92b1489e7.png?ex=685f5e12&is=685e0c92&hm=bb51a0dc0c0e3b70b2b0cbf04fc950015d3c7f8c2641a24597e5584219fcea1c&")

            log_embed = discord.Embed(
                title="__Someone has been given Trusted Player!__",
                description=f"""
> - **Given By:** {interaction.user.mention}
> - **Given to:** {user.mention}
> - **Time Given:** {config.current_time()}
> - **Reasoning:** {reason}""",
                    color=discord.Color.from_str(trust_color)
            )
            log_embed.set_image(url="https://cdn.discordapp.com/attachments/1182828263828103240/1303479711552503868/output-onlinepngtools_4-fotor-bg-remover-2024110517147.png?ex=68606694&is=685f1514&hm=9fc9712a32965271101d6b734ca4449e2260f46797c209f81cfb076d2e86c76f&")
            log_embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1182828263828103240/1345232691422957679/8f959dbeba52b3cd676f35e92b1489e7.png?ex=686006d2&is=685eb552&hm=deed5430471ab3b9bd57b4cef70502ef8d3ddd8bc1a541111c36728e421ebeb6&")
            log_embed.set_footer(icon_url="https://media.discordapp.net/attachments/1182828263828103240/1345232691422957679/8f959dbeba52b3cd676f35e92b1489e7.png?ex=686006d2&is=685eb552&hm=deed5430471ab3b9bd57b4cef70502ef8d3ddd8bc1a541111c36728e421ebeb6&", text="ASRP - /trustvip command logs.")

            await user.add_roles(self.bot.get_guild(1182487341386969158).get_role(1182827826555125802))
            await user.send(embed=trusted_embed)
            await self.bot.get_channel(config.channels.TRUSTED_VIP_LOGGING).send(embed=log_embed)

            await interaction.response.send_message("Success!", ephemeral=True)


async def setup(bot):
    await bot.add_cog(TrustVIPCog(bot))
