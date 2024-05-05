# from app.models import Session
from typing import Iterable


def _add_cors_headers(response, methods: Iterable[str]) -> None:
    allow_methods = list(set(methods))
    if "OPTIONS" not in allow_methods:
        allow_methods.append("OPTIONS")
    headers = {
        "Access-Control-Allow-Methods": ",".join(allow_methods),
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Credentials": "true",
        "Access-Control-Allow-Headers": (
            "origin, content-type, accept, "
            "authorization, x-xsrf-token, x-request-id"
        ),
    }
    response.headers.extend(headers)


def add_cors_headers(request, response):
    if request.method != "OPTIONS" and request.route:
        methods = [method for method in request.route.methods if request.route]
        _add_cors_headers(response, methods)


# async def authenticate_user(request):
#     token = request.headers.get("Authorization") or request.args.get('token')
#     request.ctx.user = None
#     if token:
#         session = await Session.get_or_none(token=token)
#         if session:
#             request.ctx.user = await session.user

