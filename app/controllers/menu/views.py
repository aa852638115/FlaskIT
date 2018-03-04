# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     views
   Description :
   Author :       潘晓华
   date：          2018/3/1
-------------------------------------------------
"""
from app.libraries.common import *
from . import menu
from flask import render_template


@menu.route('/')
@login_required
@check_menu('menu')
def menu_list():
    return render_template('menu/menulist.html')
