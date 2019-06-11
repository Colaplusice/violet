import os

from configs.base_config import Config


class TestConfig(Config):
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    DATABASE_URL = "sqlite:///" + os.path.join(BASE_DIR, 'violet.db')
