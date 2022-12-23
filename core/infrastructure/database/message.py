from sqlalchemy import Column, Integer, String
from core.infrastructure.database.sqlalchemy import Database

class Message(Database):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    text = Column(String)