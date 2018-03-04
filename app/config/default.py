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
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@127.0.0.1/dh_it'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_POOL_SIZE = None
    SQLALCHEMY_ECHO = False

    """LoginManager
    """
    SECRET_KEY = 'mbcloud&?57UDF9'


    """Redis缓存配置
    """
    REDIS_URL = "redis://127.0.0.1:6379/0"
