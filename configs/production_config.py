from configs.base_config import Config


class ProductionConfig(Config):
    DATABASE_URL = "mysql+pool://root:newpass@db/violet"
