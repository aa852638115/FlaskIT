# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     send_mail
   Description :
   Author :       潘晓华
   date：          2018/3/5
-------------------------------------------------
"""

import jwt
import datetime
from app.core.extensions import mail
from flask_mail import Message
from flask import current_app, request
from flask import render_template


class SendMail():
    """
    通用的发送邮件服务
    """

    def __init__(self, email=None):
        if isinstance(email, list):
            self.email = email
        else:
            self.email = [email]

        self.subject_prefix = current_app.config['MAIL_SUBJECT_PREFIX']
        self.sender = current_app.config['MAIL_SENDER']

    def send_forget_password(self):
        """
        发送找回密码的链接
        :param email:
        :return:
        """
        if not self.email:
            return False

        msg = Message(self.subject_prefix + '找回密码', sender=self.sender, recipients=self.email)
        send_url = 'http://%s/password/reset' % request.host
        expire_time = datetime.datetime.now() + datetime.timedelta(minutes=15)
        token = jwt.encode({"email": self.email[0], "expire_time": expire_time.strftime('%Y-%m-%d %H:%M:%S')},
                           key=current_app.config['JWT_SECRET_KEY'])
        msg.html = render_template('mail_temps/forget_password.html', send_url=send_url, token=token)
        mail.send(msg)
        return True
