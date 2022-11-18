import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY')
    print(SECRET_KEY)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    print(SQLALCHEMY_DATABASE_URI)
    SQLALCHEMY_TRACK_MODIFICATIONS= False

class DevConfig(Config):
    pass

class ProdConfig(Config):
    pass