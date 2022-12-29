from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Modify the database URL to connect to a PostgreSQL database
POSTGRES_USERNAME = "api"
POSTGRES_PASSWORD = "api"
POSTGRES_HOST = "localhost"
POSTGRES_PORT = "5432"
POSTGRES_DBNAME = "api"

SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USERNAME}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DBNAME}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={
        "connect_timeout": 10,
    },
)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)


Base = declarative_base()


def create_tables():
    Base.metadata.create_all(bind=engine)
