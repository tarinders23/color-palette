from sanic import Blueprint

from .message import message

blueprint_group = Blueprint.group(message, url_prefix="api")