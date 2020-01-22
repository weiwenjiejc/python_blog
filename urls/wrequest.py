# -*- coding: utf-8 -*-
from flask import Blueprint, request, render_template, session

from mydb.db import Mydb

wrequest = Blueprint('wrequest', __name__)

db = Mydb()


class LoginUser(object):
    username = None

@wrequest.route('/request/logout')
def logout():
    session.pop('LoginUser')
    return render_template('index.html',LoginUser=None)

@wrequest.route('/request/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    ps = db.getUserPasswd(username)
    if ps == password:
        user = {}
        user['username'] = username
        session['LoginUser'] = user
        print('测试：')
        print(type(user))
        print(user)
        return render_template('index.html',LoginUser=user)
    else:
        return render_template('msg.html',msg='密码错误，重新登录')
