from sqlalchemy import Column, String
from sqlalchemy.types import Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Dice(Base):
    __tablename__ = "dice"

    id = Column(Integer, primary_key=True)
    twitch_username = Column(String(255), unique=True)
    points = Column(Integer, default=1000)
    wins = Column(Integer, default=0)
    loses = Column(Integer, default=0)

    def __repr__(self) -> str:
        return f"<User: {self.twitch_username} | Points: {self.points} | Wins: {self.wins} | Loses: {self.loses}>"
