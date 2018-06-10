# coding=utf8
"""
-------------------------------------------------
   File Name：     views
   Description :
   Author :       潘晓华
   date：          2017/9/11
-------------------------------------------------
"""
from flask import g
from flask import request
from app.models.account import Account
from app.models.group import Group
from . import account
from app.core.extensions import db
from app.libraries.common import *


@account.context_processor
def add_item():
    g.enumerate = enumerate
    g.json = json
    return dict()

@account.route('/')
@check_menu('account')
def index(cur_parent, cur_child):
    accounts = Account.query.all()
    groups = Group.add_group_id(Group.query.all())
    return render_template('account/userlist.html', **locals())

@account.route('/account', methods=['POST'])
@login_required
def add_account():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    repassword = request.form.get('repassword')
    group_ids = request.form.get('group_ids')

    if username is None or username == '' or group_ids is None or group_ids == '[]' or email is None or email == '' or not password or not repassword:
        return u'输入有误，请检查', 502
    username = username.replace(' ', '')
    if username.find('@') != -1:
        return u'用户名不能出现"@"，请更换用户名', 502

    if password != repassword:
        return u'密码不匹配，请检查', 502

    if Account.query.filter(Account.username == username).count():
        return u'该用户名已被占用，请更换用户名', 502

    if Account.query.filter(Account.email == email).count():
        return u'该邮箱已被占用，请更换邮箱', 502

    account_item = Account(username=username, email=email, password=password, groups=group_ids.replace('"', ''))
    db.session.add(account_item)
    db.session.commit()
    return 'success'

@account.route('/account', methods=['PUT'])
@login_required
def edit_account():
    username = request.form.get('username')
    email = request.form.get('email')
    group_ids = request.form.get('group_ids')
    id = request.form.get('account_id')

    if username is None or username == '' or group_ids is None or group_ids == '[]' or email is None or email == '':
        return u'输入有误，请检查', 502
    username = username.replace(' ', '')
    if username.find('@') != -1:
        return u'用户名不能出现"@"，请更换用户名', 502

    if Account.query.filter(Account.username == username, Account.id != id).count():
        return u'该用户名已被占用，请更换用户名', 502

    if Account.query.filter(Account.email == email, Account.id != id).count():
        return u'该邮箱已被占用，请更换邮箱', 502

    account_item = Account.query.get(id)
    if not account_item:
        return u'用户不存在'
    account_item.username = username
    account_item.email = email
    account_item.groups = group_ids.replace('"', '')
    db.session.add(account_item)
    db.session.commit()
    return 'success'

@account.route('/account', methods=['DELETE'])
@login_required
def delete_account():
    id = int(request.form['id'])
    account_model = Account.query.filter(Account.id == id).first()
    if not account_model:
        return u'未找到指定的用户', 502
    db.session.delete(account_model)
    db.session.commit()
    return 'success'

@account.route('/reset/pass', methods=['PUT'])
@login_required
def reset_password():
    id = int(request.form['id'])
    password = request.form['password']
    repassword = request.form['repassword']
    if not password or len(password) < 6:
        return u'密码长度过短，要大于6位', 502
    if password != repassword:
            return u'密码不匹配，请检查', 502
    account_model = Account.query.filter(Account.id == id).first()
    if not account_model:
        return u'未找到指定的用户', 502
    account_model.set_password(password)
    db.session.commit()
    return 'success'

@account.route('/group')
@check_menu('account')
def group(cur_parent, cur_child):
    group_item = 'active'
    groups = Group.query.all()
    return render_template('account/grouplist.html', **locals())


@account.route('/group', methods=['POST'])
@login_required
def add_group():
    group_name = request.form.get('group_name')
    group_menu_ids = request.form.get('group_menu_ids')
    group_desc = request.form.get('group_desc', '')
    if group_name is None or group_name == '' or group_menu_ids is None or group_menu_ids == '[]':
        return u'输入有误，请检查', 502
    group_name = group_name.replace(' ', '')
    if Group.query.filter(Group.group_name == group_name).count():
        return u'该组已存在，请更换组名', 502
    group_item = Group(group_name=group_name, menu_ids=group_menu_ids.replace('"', ''), desc=group_desc)
    db.session.add(group_item)
    db.session.commit()
    return 'success'


@account.route('/group', methods=['PUT'])
@login_required
def edit_group():
    group_name = request.form.get('group_name')
    group_menu_ids = request.form.get('group_menu_ids')
    group_desc = request.form.get('group_desc', '')
    group_id = request.form.get('group_id', '')
    if group_name is None or group_name == '' or group_id is None or group_id == '' or group_menu_ids is None or group_menu_ids == '[]':
        return u'输入有误，请检查', 502
    group_name = group_name.replace(' ', '')
    if Group.query.filter(Group.group_name == group_name, Group.id != int(group_id)).count():
        return u'该组已存在，请更换组名', 502
    group_item = Group.query.filter(Group.id == group_id)
    group_item.update({Group.group_name: group_name, Group.desc: group_desc, Group.menu_ids: group_menu_ids.replace('"', '')})
    db.session.commit()
    return 'success'

@account.route('/group', methods=['DELETE'])
@login_required
def delete_group():
    id = int(request.form['id'])
    group_model = Group.query.filter(Group.id == id).first()
    if not group_model:
        return u'未找到指定的权限组', 502
    db.session.delete(group_model)
    db.session.commit()
    return 'success'
