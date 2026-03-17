from enum import Enum 

class Role(str, Enum):
    duelista = "duelista"
    controlador = "controlador"
    iniciador = "iniciador"
    sentinela = "sentinela"
    flex = "flex"