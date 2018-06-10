# -*- coding: utf-8 -*-
"""
----------------------------------------------------
    File Name:      __init__.py
    Description:
    Author:         潘晓华
    date:           2018/6/10
----------------------------------------------------
"""


from flask import Blueprint

dashboard = Blueprint('dashboard', __name__)

from . import views