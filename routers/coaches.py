from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Coach
from schemas import CoachCreate, CoachResponse, CoachUpdate

router = APIRouter()

@router.get("/coaches", response_model=list[CoachResponse])
def listar_coaches(db: Session = Depends(get_db)):
    coaches = db.query(Coach).all()
    return coaches

@router.get("/coaches/{id_coach}", response_model=CoachResponse)
def buscar_coach(id_coach: int, db: Session = Depends(get_db)):
    coach = db.query(Coach).filter(Coach.id_coach == id_coach).first()
    if not coach:
        raise HTTPException(status_code=404, detail="Coach not found!")
    return coach  

@router.post("/coaches", response_model=CoachResponse)
def criar_coach(coach: CoachCreate, db: Session = Depends(get_db)):
    new_coach = Coach(
        name=coach.name,
        nickname=coach.nickname,
        country=coach.country,
        social=coach.social,
        birth_date=coach.birth_date
    )
    db.add(new_coach)
    db.commit()
    db.refresh(new_coach)
    return(new_coach)

@router.patch("/coaches/{id_coach}", response_model=CoachResponse)
def atualizar_coach(id_coach: int, coach: CoachUpdate, db: Session = Depends(get_db)):
    db_coach = db.query(Coach).filter(Coach.id_coach == id_coach).first()
    if not db_coach:
        raise HTTPException(status_code=404, detail="Coach not found!")
    
    dados = coach.model_dump(exclude_unset=True)
    for campo, valor in dados.items():
        setattr(db_coach, campo, valor)

    db.commit()
    db.refresh(db_coach)
    return db_coach

@router.delete("/coaches/{id_coach}")
def deletar_coach(id_coach: int, db: Session = Depends(get_db)):
    deleted_coach = db.query(Coach).filter(Coach.id_coach == id_coach).first()
    if not deleted_coach:
        raise HTTPException(status_code=404, detail="Coach not found!")
    
    db.delete(deleted_coach)
    db.commit()
    return {"message": "Coach deleted successfully"}
    