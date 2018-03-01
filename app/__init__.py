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

from .core.extensions import db, redis


class App():
    """
    应用类
    """

    def __init__(self):
        app = Flask(__name__)
        self.app = app

        self.__init_config()
        self.__init_model()
        self.__register_all_blueprint()

    def __init_config(self):
        self.app.config.from_object(load_config())
        self.app.debug = self.app.config.get('DEBUG')

    def __init_model(self):
        db.init_app(self.app)
        redis.init_app(self.app, decode_responses=True)

    def __register_all_blueprint(self):
        # 注册controllers下所有的蓝图
        import os
        from os import sep
        for bp in os.listdir(os.getcwd() + sep + __name__ + sep + 'controllers'):
            if not bp.startswith('__'):
                bp_module = __import__(__name__ + r'.controllers' + '.' + bp, None, None, [bp])
                bp_blueprint = getattr(bp_module, bp)
                try:
                    url_prefix = bp_module.url_prefix
                except Exception as e:
                    url_prefix = bp
                self.app.register_blueprint(bp_blueprint, url_prefix='/' + url_prefix)

    def get_app(self):
        return self.app

    def run(self, *args, **kwargs):
        self.app.run(*args, **kwargs)