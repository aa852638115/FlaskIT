# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     default
   Description :
   Author :       潘晓华
   date：          2018/3/1
-------------------------------------------------
"""


class Config(object):
    DEBUG = True

    """Mysql数据库配置
    """
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://flaskit:flaskit@127.0.0.1/flaskit'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_POOL_SIZE = None
    SQLALCHEMY_ECHO = False

    """LoginManager
    """
    SECRET_KEY = 'flaskit&?57UDF9'


    """Redis缓存配置
    """
    REDIS_URL = "redis://127.0.0.1:6379/0"

    """邮箱服务器配置
    """
    MAIL_SUBJECT_PREFIX = '[DH Flask-IT]'
    MAIL_SERVER = '<Mail Server>'
    MAIL_PORT = 25
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False
    MAIL_USERNAME = "<user@mail.example.com>"
    MAIL_PASSWORD = "<password>"
    MAIL_SENDER = 'FlaskIT自动回复<user@mail.example.com>'


    """JWT加密密钥
    """
    JWT_SECRET_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9'