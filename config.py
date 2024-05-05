# Prod Config
from datetime import timedelta

REGION = "eu-west-3"
# Backend BASE URL

APP_NAME = "PLATFORM"
AUTH_TOKEN_EXPIRY = timedelta(days=30)
DB_CONFIG = dict(
    connections=dict(
        default=dict(
            engine='tortoise.backends.asyncpg',
            credentials=dict(
                host="websamp-eu.cg2gmo2o12rn.eu-west-3.rds.amazonaws.com",
                port="5432",
                # user="stag_user",
                # password="stag_pass",
                # database="websamp_stag"
                user="vikas",
                password="vikas-pass",
                database="websamp_prod"
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