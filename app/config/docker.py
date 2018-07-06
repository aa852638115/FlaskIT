# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     docker
   Description :
   Author :       潘晓华
   date：          2018/7/6
-------------------------------------------------
"""


from .default import Config
class DockerConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:flaskit@db/flaskit'

