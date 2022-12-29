from app.adapters.db import SqlAlchemyUserRepository
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.adapters.in_memory import InMemoryUserRepository
from app.api import controllers
from app.infrastructure.db import repositories

# Crea la conexión a la base de datos
repository = InMemoryUserRepository()
# Crea la aplicación FastAPI y agrega los controladores
app = FastAPI()

app.include_router(controllers.router)

