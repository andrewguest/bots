import random

from disnake.ext import commands

import steam


# Discord bot setup
bot = commands.Bot()


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
    else:
        await interaction.response.send_message(
            f"Could not find any games for: {steam_community_name}"
        )


if __name__ == "__main__":
    # TODO put this key in an environment variable
    bot.run(
        "MTAwNTU1NzUxMTM4ODEzNTUxNA.Gw-L-F.1jkRChnKHFkkTAXhslJ4xqxea65z2NMyvrhTow"
    )
