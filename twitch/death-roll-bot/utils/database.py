import os

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

from utils.models import Base, Dice


load_dotenv()  # Load environment variables from .env file

CONNECTION_STRING = os.getenv("DEATH_ROLL_DATABASE_CONNECTION_STRING") or ""

engine = create_engine(CONNECTION_STRING)
meta = MetaData(engine)
meta.create_all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def get_or_create_user(twitch_username: str):
    """Get a user by their Twitch username or create a record if one doesn't exist.

    Args:
        twitch_username (str): The Twitch username of the user to lookup or create.
    """

    user = (
        session.query(Dice)
        .filter(Dice.twitch_username == twitch_username)
        .first()
    )

    if not user:
        user = Dice(twitch_username=twitch_username)
        session.add(user)
        session.commit()

    return user


def add_points(twitch_username: str, points_to_add: int):
    """Add points to a user's record. The user needs to already exist for this to work.

    Args:
        twitch_username (str): The Twitch username of the user playing the game.
        points_to_add (int): The number of points to add to the user.
    """

    # Get the user record
    user = (
        session.query(Dice)
        .filter(Dice.twitch_username == twitch_username)
        .first()
    )

    # Increase the points
    user.points += points_to_add

    # Write the increased points to the database
    session.add(user)
    session.commit()
