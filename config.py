# Prod Config
from datetime import timedelta

REGION = "eu-west-3"
# Backend BASE URL

APP_NAME = "COLOR_PALETTE"
AUTH_TOKEN_EXPIRY = timedelta(days=30)
CHATGPT_API_KEY = ''
DB_CONFIG = dict(
    connections=dict(
        default=dict(
            engine='tortoise.backends.asyncpg',
            credentials=dict(
                host="",
                port="5432",
                user="",
                password="",
                database=""
            )
        ),
        sqlite="sqlite://testfile.db"
    ),
    apps=dict(
        app=dict(
            models=["app.models", "aerich.models"],
            default_connection='default',
        )
    ),
)