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
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail


db = SQLAlchemy()
redis = FlaskRedis()
bcrypt = Bcrypt()
mail = Mail()
login_manager = LoginManager()