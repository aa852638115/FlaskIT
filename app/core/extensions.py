# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     extensions
   Description :
   Author :       潘晓华
   date：          2018/3/1
-------------------------------------------------
"""

from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis


db = SQLAlchemy()
redis = FlaskRedis()