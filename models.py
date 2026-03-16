from database import Base
from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    nickname = Column(String, nullable=False)
    role = Column(String)
    country = Column(String)
    active = Column(Boolean, default=True)

class Coach(Base):
    __tablename__ = "coaches"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    nickname = Column(String, nullable=False)
    country = Column(String)
    active = Column(Boolean, default=True)
