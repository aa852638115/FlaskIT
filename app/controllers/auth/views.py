# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     views
   Description :
   Author :       潘晓华
   date：          2018/3/4
-------------------------------------------------
"""


from . import auth

@auth.route('/')
def index():
    return "Auth-Index"