# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     views
   Description :
   Author :       潘晓华
   date：          2018/3/1
-------------------------------------------------
"""
from . import account
from app.libraries.common import *

@account.route('/')
@check_menu('menu')
def index():
    return "Account-Index"