class Config:
    # database
    DB_CLIENT_CHARSET = "utf8mb4"
    DATABASE_URL = "mysql+pool://root:newpass@localhost/violet"
    PW_CONN_PARAMS = {"charset": DB_CLIENT_CHARSET, "stale_timeout": 1800}
