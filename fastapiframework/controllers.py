
from application.adapters.in_memory import InMemoryUserRepository
from application.domain.user import User

from fastapi import FastAPI

app = FastAPI()

vote_repository = InMemoryUserRepository()


@app.post("/user", response_model=User)
def user() -> User:
    return Vote().save(vote_repository)


@app.get("/users", response_model=int)
def votes() -> int:
    return vote_repository.total()


router = app.router
