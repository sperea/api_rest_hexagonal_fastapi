from application.adapters.in_memory import InMemoryUserRepository
from fastapi import FastAPI
from fastapiframework import controllers

repository = InMemoryUserRepository()
app = FastAPI()
app.include_router(controllers.router)
