class Colors:
    def __init__(self):
        self.RED = "#FF0000"
        self.ORANGE = "#FFA500"
        self.LIGHT_BLUE = "#4ba4e0"
        self.BLUE = "#081cb4"
        self.GREY = "#3A3B3C"
        self.GREEN = "#07b431"
        self.YELLOW = "#dfda2b"


colors = Colors()


def get_session_color(status):
    return {
        "ssd": "#f50018",
        "ssu": "#00eb00"
    }.get(status, colors.GREY)
