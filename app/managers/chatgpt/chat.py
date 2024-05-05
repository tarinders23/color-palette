import json
from openai import OpenAI
from config import CHATGPT_API_KEY


class Chat:
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

    @classmethod
    def send(cls, messages):
        response = cls._gpt_client.chat.completions.create(
            model="gpt-4-turbo",
            messages=messages,
            tools=cls._tools,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        if response.choices[0].message.tool_calls:
            return json.loads(response.choices[0].message.tool_calls[0].function.arguments)
        else:
            return json.loads(response.choices[0].message.content)

