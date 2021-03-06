import json


class Config:
    """
    Configuration class
    """
    mcpath: str = None
    worlds: list[str] = []
    log_dir_path: str = None
    out_path: str = None
    discord_token: str = None
    discord_channel: str = None

    def __init__(self, filepath: str):
        with open(filepath, "r", encoding="utf-8") as f:
            config = json.load(f)

            self.mcpath = config["mcpath"]
            self.worlds = config["worlds"]
            self.log_dir_path = config["log_dir_path"]
            self.out_path = config["out_path"]
            self.discord_token = config["discord_token"]
            self.discord_channel = config["discord_channel"]
