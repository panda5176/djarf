import json
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self) -> None:
        self.accept()

    def disconnect(self, close_code: int) -> None:
        pass

    def receive(self, text_data: str) -> None:
        message = json.loads(text_data)["message"]
        self.send(text_data=json.dumps({"message": message}))
