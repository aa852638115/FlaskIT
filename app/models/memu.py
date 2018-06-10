# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     memu
   Description :
   Author :       潘晓华
   date：          2018/3/1
-------------------------------------------------
"""

from app.core.extensions import db, redis
from app.core.redis import RedisKey
from app.libraries.common import *


class Menu(db.Model):
    """
    菜单数据表
    """
    __tablename__ = 'dh_menu'
    id = db.Column(db.Integer, primary_key=True)
    show_name = db.Column(db.String(20))
    icon = db.Column(db.String(20))
    parent = db.Column(db.INTEGER)
    level = db.Column(db.SMALLINT)
    url = db.Column(db.String(45))

    def __init__(self, show_name, icon, url, parent=None, level=0):
        self.show_name = show_name
        self.icon = icon
        self.url = url
        self.parent = parent
        self.level = level

    @classmethod
    def generate_menu_data(cls):
        """
        处理menus将它主菜单与子菜单分开
        :return:
        """
        data = redis.get(RedisKey.menu_total_key())
        data = None
        if not data:
            data = {}
            parent_menu = {}
            menus = cls.query.all()
            for menu_item in menus:
                if menu_item.level is 0:
                    data.setdefault(menu_item, [])
                    parent_menu.setdefault(menu_item.id, menu_item)
                else:
                    data.setdefault(parent_menu.get(menu_item.parent), []).append(menu_item)
            if data:
                data = sorted(data.items(), key=lambda d: d[0].id)
                redis.set(RedisKey.menu_total_key(), data)
        else:
            print(data)
            data = json.load(data)
        return data

    @classmethod
    def get_all_ids_by_ids(cls, item_ids):
        data = []
        menus_info = cls.query.filter(cls.id.in_(item_ids))
        for item in menus_info:
            data.append(item.id)
            if item.parent:
                data.append(item.parent)
        data = set(data)
        return data

    @classmethod
    def get_id_by_url_for(cls, url):
        data = cls.query.filter(cls.url == url).first()
        print(url)
        cur_child = data.id
        cur_parent = data.parent if data.parent else cur_child
        return (cur_parent, cur_child)

    def __repr__(self):
        return u'<Menu> -%d %s %d' % (self.id, self.show_name, self.level)

    @classmethod
    def clear_cache(cls):
        redis.delete(RedisKey.menu_total_key())


if __name__ == '__main__':
    pass
