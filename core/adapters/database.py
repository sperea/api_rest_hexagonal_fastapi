from core.domain.models import Message
from core.ports.apirest import IMessageAPI
from typing import Optional

class MessageDatabase(IMessageAPI):
    def get_hello_world(self, message_id: Optional[int] = None) -> Message:
        # Conectarse a la base de datos y recuperar el mensaje de "Hola mundo"
        pass