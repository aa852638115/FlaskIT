# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     __init__.py
   Description :
   Author :       潘晓华
   date：          2018/3/4
-------------------------------------------------
"""


from flask import Blueprint

auth = Blueprint('auth', __name__)
url_prefix = '/'
from . import views