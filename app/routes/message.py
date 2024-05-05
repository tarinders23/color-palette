from sanic import Blueprint, Request
from app.managers.user_chat import UserChatSession
from app.utils.common import response

message = Blueprint("message", version=1, url_prefix="message")


@message.post("/send", name="user_message_send")
async def user_message_send(request: Request):
    payload = request.json
    data = UserChatSession.send(**payload)
    # data = [
    #     {
    #         "name": "Red Dusk",
    #         "code": "#9e1a1a"
    #     },
    #     {
    #         "name": "Dusk Maroon",
    #         "code": "#800000"
    #     },
    #     {
    #         "name": "Dusk Rose",
    #         "code": "#b76e79"
    #     },
    #     {
    #         "name": "Dusk Coral",
    #         "code": "#cd5b45"
    #     },
    #     {
    #         "name": "Dusk Ruby",
    #         "code": "#9b111e"
    #     }
    # ]
    return response(data)
