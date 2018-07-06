# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     run.py
   Description :
   Author :       潘晓华
   date：          2018/2/27
-------------------------------------------------
"""

from app import App
application = App()

if __name__ == '__main__':
    application.run(host="0.0.0.0")