import datetime

def get_session_color(status):
    return {
        "ssd": "#f50018",
        "ssu": "#00eb00"
    }.get(status, colors.GREY)

def current_time():
    return f"<t:{int(datetime.datetime.now().timestamp())}:R>"

class Channels:
    def __init__(self):
        self.SERVER_STATUS = 1354553136655892500
        self.SESSION_LOGGING = 1354553136655892500
        self.DM_LOGGING = 1354553136655892500
        self.TRUSTED_VIP_LOGGING = 1354553136655892500
        self.SUPPORTERS = 1354553136655892500
        self.SUPPORTERS_LOGGING = 1354553136655892500
        self.FEEDBACK = 1354553136655892500
        self.APPLICATION_PRIO = 1354553136655892500
        self.RATING = 1354553136655892500
        self.DM_CHAT = 1354553136655892500
        self.CHATMOD_LOGGING = 1354553136655892500
        self.ADMIN_REQUESTS = 1354553136655892500
        self.BOLO_LOGGING = 1354553136655892500

class IMGs:
    def __init__(self):
        self.GREEN_SESSION_IMG = "https://media.discordapp.net/attachments/1182828263828103240/1315885485666730084/output-onlinepngtools_3.png?ex=685c181b&is=685ac69b&hm=11f2b18b38aef85cd22a73d2abea114cbf417673444e8e223774d700c1481bc5&format=webp&quality=lossless&"
        self.RED_SESSION_IMG = "https://media.discordapp.net/attachments/1182828263828103240/1315885486342017095/output-onlinepngtools.png?ex=685c181b&is=685ac69b&hm=47aa9c43c3879c08d65dbab5cfced20f4fe7fcdb9664e8a6f93c565c099bfadd&format=webp&quality=lossless&"
        self.GREY_SESSION_IMG = "https://media.discordapp.net/attachments/1182828263828103240/1315885485411008563/output-onlinepngtools_4.png?ex=685c181b&is=685ac69b&hm=9534737cd4a693e2102130f7d9e499b364e67577acb56c44e03114ab42b05567&format=webp&quality=lossless&"
        self.YELLOW_SESSION_IMG = "https://cdn.discordapp.com/attachments/1182828263828103240/1315885486123782214/output-onlinepngtools_1.png?ex=685c181b&is=685ac69b&hm=9732bc09409891e456d2c3c806c64f207ae3164475b37e6c150f1e925ddf7dc6&"
        self.BLUE_SESSION_IMG = "https://media.discordapp.net/attachments/1182828263828103240/1315885485909868554/output-onlinepngtools_2.png?ex=685c181b&is=685ac69b&hm=f0c518173a78efea60787751510a2cbcb7ac41189cf89024b026767c47836bbf&format=webp&quality=lossless&"
        self.LIGHT_BLUE_IMG = "https://media.discordapp.net/attachments/1209626216181530644/1213649404850864158/Untitled.png?ex=6863d956&is=686287d6&hm=b0c2ab7cce3045c4c4a8f06a1bed9283efc80f756cca88c60d4691ad64f2f7a4&format=webp&quality=lossless&width=678&height=16&"
        self.ORANGE_SESSION_IMG = "https://cdn.discordapp.com/attachments/1354553136655892500/1387159961976705095/output-onlinepngtools_3.png?ex=685c54e3&is=685b0363&hm=02cae42dabd4e876376ca5197412131a83247f1f4ce0713d5d40124f742cabcc&"
        self.LIGHT_GREEN_IMG = "https://cdn.discordapp.com/attachments/1182828263828103240/1303479711212634174/output-onlinepngtools_4-fotor-bg-remover-2024110517212.png?ex=6867a6d4&is=68665554&hm=221e438d49a1ed889cd4328ad73f277fd8a62569be48f335cdf5190fa1155c66&"

class Colors:
    def __init__(self):
        self.RED = "#FF0000"
        self.ORANGE = "#FFA500"
        self.LIGHT_BLUE = "#4ba4e0"
        self.BLUE = "#081cb4"
        self.GREY = "#3A3B3C"
        self.GREEN = "#07b431"
        self.YELLOW = "#dfda2b"
        self.LIGHT_GREEN = "#58f888"


channels = Channels()
imgs = IMGs()
colors = Colors()

SSD_ID = 1391568372268797973
SSU_ID = None
session_status = "ssd"

LOGO = "https://cdn.discordapp.com/attachments/1182828263828103240/1183834014465925130/file-z2wbRRQ45BNH3lmnqqBb4L3M_1.png?ex=68637c97&is=68622b17&hm=9568dec8404d2a17d70a813a1e0f4048eb142110e666ee01541b0ae9c320a36b&"


confirmation_status_messages = {
    "ssu": "Server Start Up",
    "ssd": "Server Shut Down",
    "lpp": "Low Player Ping",
    "restart": "Session Restart",
    "crash": "Server Crash",
    "update": "Server Update"
}


"""
link = discord.ui.Button(label="label", emoji="emoji", url=url)
view = discord.ui.View()
view.add_item(link)
"""