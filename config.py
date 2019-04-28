# -*- coding: UTF-8 -*-

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

    @staticmethod
    def init_app(app):
        pass


class DEVConfig(Config):
    DEBUG=True


class TestConfig(Config):
    TESTING=True


config={'development':DEVConfig, 'testing':TestConfig,'default':DEVConfig}


