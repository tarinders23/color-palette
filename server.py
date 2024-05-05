from sanic import Sanic, redirect
from tortoise.contrib.sanic import register_tortoise

from app.middleware import add_cors_headers
from app.options import setup_options
from config import DB_CONFIG, APP_NAME

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
    return redirect('/public/index.html')


app.register_listener(setup_options, "before_server_start")
# app.register_middleware(authenticate_user, "request")
app.register_middleware(add_cors_headers, "response")
# Setup Database
# register_tortoise(app, DB_CONFIG, generate_schemas=True)

###### Tortoise logging ############
# fmt = logging.Formatter(
#     fmt="%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s",
#     datefmt="%Y-%m-%d %H:%M:%S",
# )
# sh = logging.StreamHandler(sys.stdout)
# sh.setLevel(logging.DEBUG)
# sh.setFormatter(fmt)
#
# # will print debug sql
# logger_db_client = logging.getLogger("db_client")
# logger_db_client.setLevel(logging.DEBUG)
# logger_db_client.addHandler(sh)
#
# logger_tortoise = logging.getLogger("tortoise")
# logger_tortoise.setLevel(logging.DEBUG)
# logger_tortoise.addHandler(sh)
# Run App
# app.run(host="0.0.0.0", port=8000, debug=True)
