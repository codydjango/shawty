import os

class Config(object):
    APP_HOST = os.environ.get('APP_HOST', '127.0.0.1')
    APP_PORT = os.environ.get('APP_PORT', '8000')
    PG_ADDR = os.environ.get('PG_ADDR')
    PG_DB = os.environ.get('PG_DB')
    PG_USER = os.environ.get('PG_USER')
    PG_PASSWORD = os.environ.get('PG_PASSWORD')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{addr}/{db}'.format(user=PG_USER,
                                                                    pw=PG_PASSWORD,
                                                                    addr=PG_ADDR,
                                                                    db=PG_DB)



