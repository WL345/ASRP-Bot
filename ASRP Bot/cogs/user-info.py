import discord.ext.commands, requests, datetime, config


class UserInfoCog(discord.ext.commands.Cog):
    @discord.app_commands.command(name="user-info", description="Get some information of a given Roblox user!")
    @discord.app_commands.describe(user_id="The Roblox ID of the user.")
    async def user_info(self, interaction: discord.Interaction, user_id: str):
        try:
            print(f"\n{interaction.user.name} - <@{interaction.user.id}> - Used the userinfo command")

            request = requests.get(f"https://users.roblox.com/v1/users/{user_id}")
            embed = discord.Embed(
                title=f"<:Roblox:1229446548342177792> | {request.json()["name"]}'s Information",
                description=f"""
    > - **Username:** [`{request.json()["name"]}`](https://www.roblox.com/users/{user_id}/profile)
    > - **Display Name:** `{request.json()["displayName"]}`
    > - **Roblox ID:** `{user_id}`
    > - **Roblox Description:** `{request.json()["description"] or 'None Given'}`
    > - **Account Created:** <t:{int((datetime.datetime.strptime(request.json()["created"], "%Y-%m-%dT%H:%M:%S.%fZ") - datetime.datetime(1970, 1, 1)).total_seconds())}:F>
    > - **Banned On Roblox:** `{str(request.json()["isBanned"])}`""",
                color=discord.Color.from_str(config.colors.LIGHT_BLUE)
            )
            embed.set_image(url=config.imgs.LIGHT_BLUE_IMG)
            avatar = requests.get(f"https://thumbnails.roblox.com/v1/users/avatar?userIds={user_id}&size=420x420&format=Png")
            embed.set_thumbnail(url=avatar.json()["data"][0]["imageUrl"])

            await interaction.response.send_message(embed=embed, ephemeral=True)

        except Exception as e:
            print(e)

async def setup(bot):
    await bot.add_cog(UserInfoCog())
