import os


# default config
class BaseConfig(object):
    """docstring for BaseConfig."""
    DEBUG = False
    SECRET_KEY = 'j\x1bx\xd82&d\xbd)h\xa0A\
    xe9\xb7t\x0b\x15\xa8\xda\x06\xbd\xb2a_'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
