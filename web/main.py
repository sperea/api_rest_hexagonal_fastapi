from fastapi import FastAPI
from core.domain.services import MessageService
from core.domain.ports import IMessageAPI


app = FastAPI()

@app.get("/hello")
def hello_world():
    message_service = MessageService()
    message = message_service.get_hello_world()
    return {"message": message.text}