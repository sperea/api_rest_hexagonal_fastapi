from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .domain import User, UserRepository

# Crea la conexión a la base de datos
DATABASE_URI = "postgresql://user:password@localhost/database"
engine = create_engine(DATABASE_URI)
Base = declarative_base()
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

class SqlAlchemyUserRepository(UserRepository):
    def __init__(self, session):
        self.session = session

    def create_user(self, user: User) -> int:
        self.session.add(user)
        self.session.commit()
        return user.id

    def get_user(self, user_id: int) -> User:
        return self.session.query(User).filter(User.id == user_id).first()

    def update_user(self, user: User) -> User:
        self.session.add(user)
        self.session.commit()
        return user

    def delete_user(self, user_id: int) -> None:
        self.session.query(User).filter(User.id == user_id).delete()
        self.session.commit()