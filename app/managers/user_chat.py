import json

from app.managers.chatgpt.chat import Chat


class User:
    def __init__(self, user_id):
        self.user_id = user_id
        self.messages = [
            {
                "role": "system",
                "content": "You are color palette assistant. And show 5 hex color codes"
             }
        ]


class UserChatSession:
    user_map = {}

    @classmethod
    def send(cls, user_id, message):
        if cls.user_map.get(user_id) is None:
            cls.user_map[user_id] = User(user_id)

        user = cls.user_map.get(user_id)
        user.messages.append({
            "role": "user",
            "content": message
        })

        response = Chat.send(user.messages)
        user.messages.append({
            "role": "system",
            "content": json.dumps(response)
        })

        return response.get('color_codes')
