# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     views
   Description :
   Author :       潘晓华
   date：          2018/3/1
-------------------------------------------------
"""
from . import menu
from app.models.memu import Menu as MenuModel


@menu.route('/')
def index():

    print(MenuModel.generate_menu_data())
    return 'hello'