import os

SECRET_KEY = '123'
SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/latte.db' % os.path.dirname(__file__)
SQLALCHEMY_ECHO = False
DEBUG = True
