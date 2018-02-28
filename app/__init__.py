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
from .config import load_config

def create_app():
    app = Flask(__name__)
    app.config.from_object(load_config())
    app.debug = app.config.get('DEBUG')

    @app.route("/")
    def hello():
        return "Hello!"

    return app