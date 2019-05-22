import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # DB section
    MONGODB_SETTINGS = {
        'db': 'first_database',
        'host': 'localhost',
        'port': 27017,
    }

    # JWT section
    # JWT_TOKEN_LOCATION = 'cookies'
    # JWT_COOKIE_SECURE = False
    # JWT_ACCESS_COOKIE_PATH = '/api/'
    # JWT_REFRESH_COOKIE_PATH = '/token/refresh'
    # JWT_COOKIE_CSRF_PROTECT = False
    # JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    # JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(hours=24)
    # JWT_SESSION_COOKIE = False
