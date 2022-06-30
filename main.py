import discord

import logging
import os

from utils.bot import MyClient


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("discord")
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s"))
logger.addHandler(handler)


client = MyClient()


cog_directories = ['./commands', './events']

for i in range(2):
    for directory in [cog_directories[i][2:]]:
        for file in os.listdir(directory):
            if file.endswith(".py"):
                client.load_extension(f"{directory}.{file[:-3]}")


if __name__ == "__main__":
    client.run("OTkxODI5MDk0MDM3NzI1MjQ0.GPWW8p.L_jyyOoPFfLOWKddp99kV5ZteznnoC3MdwEcqw")

