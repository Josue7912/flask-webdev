import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = "Keep it a secret, at all costs"
    SQLALCHEMY_DATABASE_URI = \
        f'sqlite:///{os.path.join(basedir, "data-dev.sqlite")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS =  True

    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    RAGTIME_ADMIN = os.environ.get('RAGTIME_ADMIN')
    RAGTIME_MAIL_SUBJECT_PREFIX = 'Ragtime - '
    RAGTIME_MAIL_SENDER = f'Ragtime Admin <(RAGTIME_ADMIN)>'

    RAGTIME_COMPS_PER_PAGE = 20
    RAGTIME_FOLLOWERS_PER_PAGE = 5
    RAGTIME_FOLLOWING_PER_PAGE = 5

    def init_app(app):
        pass

config = {'default': Config}