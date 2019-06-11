from datetime import timedelta

from configs.base_config import Config


class DevConfig(Config):
    # 缓存
    DEBUG = True
    SEND_FILE_MAX_AGE_DEFAULT = timedelta(1)
