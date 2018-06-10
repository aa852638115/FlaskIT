# -*- coding: utf-8 -*-
"""
----------------------------------------------------
    File Name:      views
    Description:
    Author:         潘晓华
    date:           2018/6/10
----------------------------------------------------
"""
from app.libraries.common import *
from . import dashboard
from flask import render_template

@dashboard.route('/')
@check_menu('dashboard')
def dashboard(cur_parent, cur_child):
    return render_template('dashboard/index.html', **locals())