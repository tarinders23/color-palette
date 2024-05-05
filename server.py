from sanic import Sanic, redirect

from app.middleware import add_cors_headers
from app.options import setup_options
from config import APP_NAME

app = Sanic(name=APP_NAME)
app.config.FALLBACK_ERROR_FORMAT = "json"
app.config.DEBUG = True
app.static('/public', './static')

from app.routes import blueprint_group

app.blueprint(blueprint_group)
for route in app.router.routes_all:
    print(route)


@app.route('/', methods=["GET"])
async def handler(request):
    return redirect('/public/index.html?user_id=tarinder')


app.register_listener(setup_options, "before_server_start")
# app.register_middleware(authenticate_user, "request")
app.register_middleware(add_cors_headers, "response")
