# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     __init__.py
   Description :
   Author :       潘晓华
   date：          2018/3/1
-------------------------------------------------
"""


from flask import Blueprint

account = Blueprint('account', __name__)
# url_prefix = '/account'

from . import views