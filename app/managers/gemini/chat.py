import json
import google.generativeai as genai
from config import GEMINI_API_KEY

initial_prompt = """You are a color code assistant. Always provide a list of color name and its hex color code in JSON format only no markdown. The output should contain upto 5 colours

Example response: 
[
        {
            "name": "Red Dusk",
            "code": "#9e1a1a"
        },
        {
            "name": "Dusk Maroon",
            "code": "#800000"
        },
        {
            "name": "Dusk Rose",
            "code": "#b76e79"
        },
        {
            "name": "Dusk Coral",
            "code": "#cd5b45"
        },
        {
            "name": "Dusk Ruby",
            "code": "#9b111e"
        }
]


"""

class GeminiChat:
    _genai = genai.configure(api_key=GEMINI_API_KEY)
    _user_chat_map = {}

    @classmethod
    def send(cls, user_id, message):
        if cls._user_chat_map.get(user_id) is None:
            model = genai.GenerativeModel('gemini-pro')
            chat = model.start_chat(history=[])
            cls._user_chat_map[user_id] = chat
            message = initial_prompt + message

        chat = cls._user_chat_map.get(user_id)
        response = chat.send_message(message)
        print("Gemini Response: ", response.text)
        return json.loads(response.text)


