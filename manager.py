# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     manager
   Description :
   Author :       潘晓华
   date：          2018/3/1
-------------------------------------------------
"""

from app import App
from flask_script import Manager
app = App().get_app()
manager = Manager(app)

if __name__=='__main__':
    manager.run()