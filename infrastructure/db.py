from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base
import os

# Récupération de la configuration depuis les variables d'environnement
DB_USER = os.getenv("POSTGRES_USER", "postgres")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")
DB_HOST = os.getenv("POSTGRES_HOST", "db")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")
DB_NAME = os.getenv("POSTGRES_DB", "postgres")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
# Les modèles ORM doivent hériter de Base
# Exemple :
# class MyModel(Base):
#     __tablename__ = "my_table"
#     id = Column(Integer, primary_key=True)

# Fonction utilitaire pour obtenir une session (à utiliser dans les dépendances FastAPI)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 