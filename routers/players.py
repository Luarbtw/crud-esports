from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Player
from schemas import PlayerCreate, PlayerResponse, PlayerUpdate

router = APIRouter()
#consulta uma lista de todos os players
@router.get("/players", response_model=list[PlayerResponse])
def listar_players(db: Session = Depends(get_db)):
    players = db.query(Player).all()
    return players 

#consulta um player pelo id
@router.get("/players/{id_player}", response_model=PlayerResponse)
def buscar_player(id_player: int, db: Session = Depends(get_db)):
    player = db.query(Player).filter(Player.id_player == id_player).first()
    if not player:
        raise HTTPException(status_code=404, detail="Player not found!")
    return player

#cria um novo player
@router.post("/players", response_model=PlayerResponse)
def criar_player(player: PlayerCreate, db: Session = Depends(get_db)):
    new_player = Player(
        name=player.name,
        nickname=player.nickname,
        country=player.country,
        role=player.role,
        social=player.social,
        birth_date=player.birth_date
    )
    db.add(new_player)
    db.commit()
    db.refresh(new_player)
    return(new_player)

#atualiza um player
@router.patch("/players/{id_player}", response_model=PlayerResponse)
def atualizar_player(id_player: int, player: PlayerUpdate, db: Session = Depends(get_db)):
    db_player = db.query(Player).filter(Player.id_player == id_player).first()
    if not db_player:
        raise HTTPException(status_code=404, detail="Player not found!")
    
    dados = player.model_dump(exclude_unset=True)
    for campo, valor in dados.items():
        setattr(db_player, campo, valor)

    db.commit()
    db.refresh(db_player)
    return db_player    

#deleta um player
@router.delete("/players/{id_player}")
def deletar_player(id_player: int, db: Session = Depends(get_db)):
    deleted_player = db.query(Player).filter(Player.id_player == id_player).first()
    if not deleted_player:
        raise HTTPException(status_code=404, detail="Player not found!")
    
    db.delete(deleted_player)
    db.commit()
    return {"message": "Player deleted successfully"}