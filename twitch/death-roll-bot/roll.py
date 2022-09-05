from typing import List, Dict
import random


def deathroll(user: str) -> str:
    """Death roll game from NoPixel.

    Args:
        user (str): The user that is challenging dice god.

    Returns:
        str: A message containing who won the game and all of the rolls.
    """
    dicegod_won = False  # has Dice God won?
    user_won = False  # has the user won?
    current_max = 1000  # high end of the range to pick from
    twitch_message = ""  # the message to return to the Twitch user
    rolls: List[
        Dict[str, int]
    ] = (
        []
    )  # each roll is a dictionary containing the name of the roller and their roll

    while not dicegod_won and not user_won:
        for player in ["Dice God", user]:
            current_roll = random.randint(1, current_max)
            rolls.append({player: current_roll})
            if current_roll == 1:
                if player == "Dice God":
                    user_won = True
                    break
                else:
                    dicegod_won = True
                    break
            else:
                current_max = current_roll

    if user_won:
        twitch_message += f"Congrats {user}, you beat Dice god!\n\n"
    else:
        twitch_message += f"Sorry {user}, Dice God won.\n\n"

    # Append the rolls to 'twitch_message', check if we're at the end of the list
    #   of rolls. The last item in 'rolls' has a slightly different string added.
    for index, dice_roll in enumerate(rolls):
        for key, value in dice_roll.items():
            if index == len(rolls) - 1:
                twitch_message += f"{key}: {value}"  # no more elements, so no space and pipe characters
            else:
                twitch_message += f"{key}: {value} | "

    print(twitch_message)
    return twitch_message


deathroll("bob")
