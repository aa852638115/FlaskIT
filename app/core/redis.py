# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     redis
   Description :
   Author :       潘晓华
   date：          2018/3/1
-------------------------------------------------
"""


class RedisKey(object):
    """
    Redis的键管理类
    """

    @classmethod
    def menu_total_key(cls):
        return 'MENU_TOTAL_KEY'