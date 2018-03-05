# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     group
   Description :
   Author :       潘晓华
   date：          2018/3/4
-------------------------------------------------
"""
from app.libraries.common import *
from app.core.extensions import db
from app.models.memu import Menu


class Group(db.Model):
    """
    权限组
    """
    __tablename__ = 'dh_group'
    id = db.Column(db.INTEGER, primary_key=True)
    group_name = db.Column(db.String(20))
    menu_ids = db.Column(db.String(45))
    desc = db.Column(db.TEXT)

    def __init__(self, group_name, menu_ids, desc):
        self.group_name = group_name
        self.menu_ids = menu_ids
        self.desc = desc

    @classmethod
    def add_group_id(cls, groups):
        data = {}
        for group_item in groups:
            data[group_item.id] = group_item
        return data

    @classmethod
    def get_all_ids_by_ids(cls, groups):
        menus = []
        groups_info = cls.query.filter(cls.id.in_(groups))
        for item in groups_info:
            menus = menus + json.loads(item.menu_ids)
        menus_set = set(menus)
        return Menu.get_all_ids_by_ids(menus_set)
