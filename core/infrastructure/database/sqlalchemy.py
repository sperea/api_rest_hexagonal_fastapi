import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Database:
    def __init__(self):
        # Crea una engine de SQLAlchemy que se conecte a la base de datos.
        # En este ejemplo, se asume que la base de datos es una base de datos
        # de PostgreSQL y que se encuentra en el host "localhost" y tiene
        # un usuario y contraseña.
        self.engine = create_engine(
            "postgresql://user:password@localhost/database"
        )
        # Crea una sesión de SQLAlchemy para realizar operaciones de persistencia.
        self.Session = sessionmaker(bind=self.engine)

    def create_tables(self):
        # Crea las tablas en la base de datos utilizando las clases declarativas
        # de SQLAlchemy definidas en la aplicación.
        Base.metadata.create_all(self.engine)