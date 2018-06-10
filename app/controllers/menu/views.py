# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     views
   Description :
   Author :       潘晓华
   date：          2018/3/1
-------------------------------------------------
"""
from app.core.extensions import db
from app.libraries.common import *
from . import menu
from flask import render_template, request


@menu.route('/')
@login_required
@check_menu('menu')
def menu_list(cur_parent, cur_child):
    return render_template('menu/menulist.html', **locals())


@menu.route('/menu', methods=['POST'])
def add_menu():
    """
    添加菜单
    :return:添加成功
    """
    show_name = request.form.get('show_name')
    icon = request.form.get('icon')
    parent = request.form.get('parent')
    level = request.form.get('level')
    url = request.form.get('url')
    if show_name is None or level is None or not level.isdigit():
        return u'输入有误', 502
    show_name = show_name.replace(' ', '')
    if parent:
        parent = int(parent)

    if Menu.query.filter(Menu.show_name == show_name).count():
        return u'显示名称不能重复', 502
    if not url:
        url = None
    if not icon:
        icon = None
    level = int(level)
    if level == 1 and parent is None:
        return u'输入有误', 502

    menu_item = Menu(show_name=show_name, icon=icon, url=url, parent=parent,level=level)
    Menu.clear_cache()
    db.session.add(menu_item)
    db.session.commit()
    return 'success'
