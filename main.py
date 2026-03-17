from fastapi import FastAPI
from database import Base, engine
from routers.players import router as players_router
from routers.coaches import router as coaches_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(players_router)
app.include_router(coaches_router)