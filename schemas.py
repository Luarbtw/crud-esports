from pydantic import BaseModel
from typing import Optional
from datetime import date
from enums import Role

class PlayerCreate(BaseModel):
    name: str
    nickname: str
    country: str
    role: Optional[Role] = None
    social: Optional[str] = None
    birth_date: Optional[date] = None

class PlayerResponse(BaseModel):
    id_player: int
    name: str
    nickname: str
    country: str
    role: Optional[Role] = None
    social: Optional[str] = None
    birth_date: Optional[date] = None
    active: bool = True

    class Config:
        from_attributes = True

class PlayerUpdate(BaseModel):
    name: Optional[str] = None
    nickname: Optional[str] = None
    country: Optional[str] = None
    role: Optional[Role] = None
    social: Optional[str] = None
    birth_date: Optional[date] = None
    active: Optional[bool] = None

class CoachCreate(BaseModel):
    name: str
    nickname: str
    country: str
    social: Optional[str] = None
    birth_date: Optional[date] = None

class CoachResponse(BaseModel):
    id_coach: int
    name: str
    nickname: str
    country: str
    social: Optional[str] = None
    birth_date: Optional[date] = None
    active: bool = True

    class Config:
        from_attributes = True

class CoachUpdate(BaseModel):
    name: Optional[str] = None
    nickname: Optional[str] = None
    country: Optional[str] = None
    social: Optional[str] = None
    birth_date: Optional[date] = None
    active: Optional[bool] = None






