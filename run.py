# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     run.py
   Description :
   Author :       潘晓华
   date：          2018/2/27
-------------------------------------------------
"""

from app import create_app

if __name__ == '__main__':
    app = create_app()
    app.run()