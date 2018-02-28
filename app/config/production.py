# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     production
   Description :
   Author :       潘晓华
   date：          2018/3/1
-------------------------------------------------
"""


from .default import Config
class ProductionConfig(Config):
    DEBUG = False
