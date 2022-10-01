import logging
import logging.handlers
import random

from disnake.ext import commands
import yaml

import steam


# Parse the config.yaml file
with open("./config/config.yaml", "r") as file:
    config_settings = yaml.safe_load(file)

# Create Discord bot instance
bot = commands.Bot()

# Logging setup
logging_format = logging.Formatter(
    config_settings["logging"]["format"]
    or "%(asctime)s %(name)s %(levelname)s %(message)s"
)

logfile_location = (
    f'{config_settings["logging"]["directory"]}/steam-game-picker.log'
)

handler = logging.handlers.TimedRotatingFileHandler(
    logfile_location, when="midnight", backupCount=10
)
handler.setFormatter(logging_format)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(handler)


@bot.slash_command(
    name="random-game",
    description="Picks a random game from the inventory of the provided Steam user",
)
async def pick_random_game(interaction, steam_community_name: str):
    game_grabber = steam.SteamGameGrabber()
    results = game_grabber.call_all(steam_community_name)

    if isinstance(results, dict):
        await interaction.response.send_message(
            f"Your random game:\n **{random.choice(list(results.keys()))}**"
        )
        logger.info(
            f"SUCCESS - Invoked by: {interaction.author} | Steam user provided: {steam_community_name}"
        )
    else:
        await interaction.response.send_message(
            f"Could not find any games for: {steam_community_name}"
        )
        logger.error(
            f"FAILED - Invoked by: {interaction.author} | Steam user provided: {steam_community_name} | Error message: {results}"
        )


if __name__ == "__main__":
    bot.run(config_settings["discord"]["token"])
