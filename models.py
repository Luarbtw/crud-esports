from database import Base
from sqlalchemy import Column, String, Integer, Boolean, Date

class Player(Base):
    __tablename__ = "players"

    id_player = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    nickname = Column(String, nullable=False)
    role = Column(String)
    country = Column(String)
    active = Column(Boolean, default=True)
    social = Column(String)
    birth_date = Column(Date)

class Coach(Base):
    __tablename__ = "coaches"

    id_coach = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    nickname = Column(String, nullable=False)
    country = Column(String)
    active = Column(Boolean, default=True)
    social = Column(String)
    birth_date = Column(Date)