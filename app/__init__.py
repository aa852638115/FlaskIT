# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     __init__
   Description :
   Author :       潘晓华
   date：          2018/2/28
-------------------------------------------------
"""

from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello():
        return "Hello"

    return app