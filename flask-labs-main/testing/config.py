import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = "Keep it a secret, at all costs"
    SQLALCHEMY_DATABASE_URI = \
        f'sqlite:///{os.path.join(basedir, "data-dev.sqlite")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    def init_app(app):
        pass

config = {'default': Config}