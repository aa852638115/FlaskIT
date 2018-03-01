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

menu = Blueprint('menu', __name__)

from . import views