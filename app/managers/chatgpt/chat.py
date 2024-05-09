import json
from openai import OpenAI
from config import CHATGPT_API_KEY


class GptUser:
    def __init__(self, user_id):
        self.user_id = user_id
        self.messages = [
            {
                "role": "system",
                "content": "You are color palette assistant. And show 5 hex color codes"
             }
        ]


class ChatGPT:
    _gpt_client = OpenAI(api_key=CHATGPT_API_KEY)
    _tools = [
      {
        "type": "function",
        "function": {
          "name": "get_color_codes",
          "description": "Top 5 color codes",
          "parameters": {
            "type": "object",
            "properties":{
                "color_codes": {
                    "type": "array",
                    "items":{
                        "type": "object",
                        "properties": {
                            "name": {
                                "type": "string",
                                "description": "Name of the color"
                              },
                            "code": {
                                "type": "string",
                                "description": "Hex code of the color"
                              }

                        },
                        "required":["name", "code"]
                    }
                }
            },
            "required":["color_codes"]

          }
        }
      }
  ]
    user_map = {}

    @classmethod
    def send(cls, user_id, message):
        if cls.user_map.get(user_id) is None:
            cls.user_map[user_id] = GptUser(user_id)

        user = cls.user_map.get(user_id)
        user.messages.append({
            "role": "user",
            "content": message
        })

        response = cls._gpt_client.chat.completions.create(
            model="gpt-4-turbo",
            messages=user.messages,
            tools=cls._tools,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        if response.choices[0].message.tool_calls:
            result = json.loads(response.choices[0].message.tool_calls[0].function.arguments)
        else:
            result = json.loads(response.choices[0].message.content)

        user.messages.append({
            "role": "system",
            "content": json.dumps(result)
        })

        return result.get('color_codes')

