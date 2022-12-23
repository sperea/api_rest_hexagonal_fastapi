from typing import Optional

from core.domain.models import Message

class IMessageAPI:
    def get_hello_world(self, message_id: Optional[int] = None) -> Message:
        pass