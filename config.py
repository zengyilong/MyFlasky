# -*- coding:utf-8 -*-
import os

basedir = os.path.abspath(os.path.dirname(__name__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <test**@hotmail.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN') or 'test**@hotmail.com'

    #避免warning
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp-mail.outlook.com'
    MAIL_PORT = 587
    MAIL_USE_TL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'tes**y@hotmail.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or '******'
    SQLALCHEMY_DATABASE_URI =os.environ.get('DEV_DATABASE_URL') or  \
                             'sqlite:///'+os.path.join(basedir, 'data.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                               'sqlite:///'+os.path.join(basedir, 'data.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI =os.environ.get('DATABASE_URL') or  \
                             'sqlite:///'+os.path.join(basedir, 'data.sqlite')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}