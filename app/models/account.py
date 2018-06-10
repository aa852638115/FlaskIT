# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     account
   Description :
   Author :       潘晓华
   date：          2018/3/4
-------------------------------------------------
"""
import hashlib
from app.libraries.common import *
import random
import datetime
from app.core.extensions import bcrypt
from flask_login import AnonymousUserMixin

from app.core.extensions import db
from app.models.group import Group
from app.models.memu import Menu


class Account(db.Model):
    """
    用户账号
    """
    __tablename__ = 'dh_account'

    id = db.Column(db.INTEGER, primary_key=True)
    username = db.Column(db.String(45), nullable=False, unique=True)
    email = db.Column(db.String(45), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    salt = db.Column(db.String(45))
    reg_time = db.Column(db.DATETIME)
    groups = db.Column(db.String(128), default='[]')

    def __init__(self, username, email, password, groups=groups):
        self.username = username
        self.email = email
        self.salt = hashlib.sha1(str(random.random())).hexdigest()
        self.password = bcrypt.generate_password_hash(password + self.salt)
        self.reg_time = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
        self.groups = groups

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password + self.salt)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password+self.salt)

    def is_authenticated(self):
        if isinstance(self, AnonymousUserMixin):
            return False
        else:
            return True

    def is_active(self):
        return True

    def is_anonymous(self):
        if isinstance(self, AnonymousUserMixin):
            return True
        else:
            return False

    def get_id(self):
        return self.id

    def get_all_items(self):
        menu_ids = Group.get_all_ids_by_ids(json.loads(self.groups))
        return menu_ids

    def get_all_menus(self):
        return Menu.generate_menu_data()

    def get_groups(self):
        group_ids = json.loads(self.groups)
        return Group.query.filter(Group.id.in_(group_ids))

    def check_permission(self, child_id):
        """
        检测用户是否有权限
        :param child_id:
        :return:
        """
        menu_ids = Group.get_all_ids_by_ids(json.loads(self.groups))
        if child_id in menu_ids:
            return True
        else:
            return False