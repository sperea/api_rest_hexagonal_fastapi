from app.adapters.api_adapter import SqlAlchemyUserRepository
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.api import controllers
from app.infrastructure.db import repositories

# Crea la conexión a la base de datos
DATABASE_URI = "postgresql://api:api@localhost/api"
engine = create_engine(DATABASE_URI)
Base = declarative_base()
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

# Crea la aplicación FastAPI y agrega los controladores
app = FastAPI()
app.include_router(controllers.router)

# Crea la instancia del repositorio de usuarios y la pasa al servicio de usuarios
session = Session()
user_repository = SqlAlchemyUserRepository(session)
user_service = controllers.UserService(user_repository)