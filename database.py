from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# endereço do banco - vai criar um arquivo valorant.db na pasta do projeto
SQLALCHEMY_DATABASE_URL = "sqlite:///./valorant.db"

# cria a conexão com o banco
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# fábrica de sessões - abre e fecha conexão a cada requisição
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# classe pai que todos os models vão herdar
Base = declarative_base()

# função que o FastAPI usa para gerenciar a sessão automaticamente
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
