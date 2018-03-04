# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     common
   Description :
   Author :       潘晓华
   date：          2018/3/1
-------------------------------------------------
"""

import json
from flask_login import login_required
from functools import wraps
from flask import render_template
from flask_login import current_user
from app.models.memu import Menu

def check_menu(urlname):
    def func_wrapper(func):
        @wraps(func)
        def return_wrapper(*args, **kwargs):
            (cur_parent, cur_child) = Menu.get_id_by_url_for(urlname + '.' + func.__name__)
            if not current_user.check_permission(cur_child):
                return render_template('httperror/nopermission.html')
            return func(cur_parent, cur_child, *args, **kwargs)
        return return_wrapper
    return func_wrapper

