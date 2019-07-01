import os


class Config:
    # database
    DB_CLIENT_CHARSET = "utf8mb4"

    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    DATABASE_URL = "sqlite:///" + os.path.join(BASE_DIR, 'violet.db')
    PW_CONN_PARAMS = {"charset": DB_CLIENT_CHARSET, "stale_timeout": 1800}
    SECRET_KEY = 'fanjialiang2401'
