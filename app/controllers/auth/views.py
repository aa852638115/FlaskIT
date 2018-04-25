# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     views
   Description :
   Author :       潘晓华
   date：          2018/3/4
-------------------------------------------------
"""

from flask import render_template, request, current_app
from flask_login import login_user, logout_user
import datetime
import jwt
from app.models.account import Account
from app.core.extensions import db
from . import auth


@auth.route('/')
def index():
    return render_template('auth/login.html')


@auth.route('login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username.find('@') > 0:
        account_info = Account.query.filter(Account.email == username).first()
    else:
        account_info = Account.query.filter(Account.username == username).first()
    if None == account_info:
        return u'账号不存在', 502

    if not account_info.check_password(password):
        return u'密码错误', 502

    login_user(account_info)
    return 'success'


@auth.route('logout', methods=['POST'])
def logout():
    try:
        logout_user()
    except:
        pass
    return 'success'


@auth.route('password/forget', methods=['GET'])
def forget_password():
    return render_template('login/forget_password.html')


@auth.route('password/reset', methods=['GET'])
def reset_password():
    token = request.args.get('token')
    data = check_token(token=token)
    if not isinstance(data, dict):
        return render_template('httperror/error.html', msg=data)
    email = data['email']
    return render_template('login/reset_password.html', **locals())


def check_token(token):
    try:
        token_json = jwt.decode(token, key=current_app.config['JWT_SECRET_KEY'])
        email = token_json.get('email')
        expir_date = datetime.datetime.strptime(token_json.get('expire_time'), '%Y-%m-%d %H:%M:%S')
        now = datetime.datetime.now()
        if now < expir_date:
            return {"email": email}
        else:
            return u'链接已过期'
    except:
        return u'无效请求'


@auth.route('password/reset', methods=['PUT'])
def do_reset_password():
    token = request.form.get('token')
    password = request.form.get('password')
    repassword = request.form.get('repassword')
    data = check_token(token=token)
    if not isinstance(data, dict):
        return u'链接已经过期了', 502
    email = data['email']
    if not password or not repassword:
        return u'输入有误，请检查', 502
    if len(password) < 6:
        return u'密码长度过短，要大于6位', 502

    if password != repassword:
        return u'密码不匹配，请检查', 502

    account = Account.query.filter(Account.email == email).first()
    if not account:
        return u'用户不存在', 502
    account.set_password(password=password)
    db.session.add(account)
    db.session.commit()
    return 'success'


@auth.route('password/reset', methods=['POST'])
def send_email():
    email = request.form.get('email')
    if not Account.query.filter(Account.email == email).count():
        return u'未找到用户', 502
    send_mail = SendMail(email=email)
    send_mail.send_forget_password()
    return 'success'
