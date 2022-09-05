import logging
import logging.handlers
import os
import random

from dotenv import load_dotenv
from disnake.ext import commands

import steam


# Setup
load_dotenv()  # Load environment variables from the .env file
bot = commands.Bot()

# Logging setup
logging_format = logging.Formatter(
    os.getenv('STEAM_GAME_PICKER_LOGFILE_NAME_FORMAT')
    or '%(asctime)s %(name)s %(levelname)s %(message)s'
)
logfile_location = f'{os.getenv("STEAM_GAME_PICKER_LOGGING_DIR")}/steam-game-picker.log'

handler = logging.handlers.TimedRotatingFileHandler(logfile_location, when="S", interval=30, backupCount=10)
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
        logger.info(f'SUCCESS - Invoked by: {interaction.author} | Steam user provided: {steam_community_name}')
    else:
        await interaction.response.send_message(
            f"Could not find any games for: {steam_community_name}"
        )
        logger.error(f'FAILED - Invoked by: {interaction.author} | Steam user provided: {steam_community_name} | Error message: {results}')


if __name__ == "__main__":
    bot.run(os.getenv("STEAM_GAME_PICKER_DISCORD_TOKEN"))
