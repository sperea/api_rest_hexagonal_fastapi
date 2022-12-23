from .models import Message

class MessageService:
    def get_hello_world(self) -> Message:
        return Message("Hola mundo")