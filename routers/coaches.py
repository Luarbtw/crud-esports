from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Coach
from schemas import CoachCreate, CoachResponse, CoachUpdate