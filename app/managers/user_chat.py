import json

from sanic import BadRequest

from app.managers.chatgpt.chat import ChatGPT
from app.managers.gemini.chat import GeminiChat

class UserChatSession:
    chat_map = {
        "chat_gpt": ChatGPT,
        "gemini": GeminiChat
    }


    @classmethod
    def send(cls, user_id, message, chat_provider):
        chat = cls.chat_map.get(chat_provider, GeminiChat)
        return chat.send(user_id, message)
