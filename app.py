# -*- coding: utf-8 -*-
from datetime import datetime

from flask import Flask, render_template, request, Response, json, jsonify, session
from flask_migrate import MigrateCommand, Migrate
from flask_script import Manager, Server
from flask_sqlalchemy import SQLAlchemy

from ext import init
from mydb.db import Mydb
from settings import MyConfig
from urls.my_sql import wsql
from urls.user import user
from urls.whtml import whtml
from urls.wrequest import wrequest

app = Flask(__name__)
app.register_blueprint(user)
app.register_blueprint(wsql)
app.register_blueprint(whtml)
app.register_blueprint(wrequest)

app.config.from_object(MyConfig)

db = Mydb()

@app.route('/')
def default_html():
    LoginUser = session.get('LoginUser')
    return render_template('index.html',LoginUser=LoginUser)


@app.route('/index_h')
def index_h():
    return render_template('index2.html')





@app.route('/index1')
def index1():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/posts_r')
def posts_r():
    pass


@app.route('/list_post_h')
def list_post_h():
    # dbb = Mydb()
    rs = db.getPost(0, 3)
    print(rs)
    pages = db.getPostCount()
    f = pages % 3
    if f == 0:
        pages = pages // 3
    else:
        pages = pages // 3 + 1
    LoginUser = session.get('LoginUser')
    return render_template('list_post.html', LoginUser=LoginUser,page_num=0 + 1, post_list=rs, pages=pages + 1)
    # return Response('msg')


@app.route('/list_post', methods=['GET'])
def list_post():
    # dbb = Mydb()
    start_page = request.args.get('startPage')
    page_count = request.args.get('pageCount')
    if start_page == None:
        start_page = 0
        page_count = 5
    print(start_page)
    print(page_count)
    rs = db.getPost(int(start_page), int(page_count))
    print('ddd:')
    print(jsonify(rs))
    print(rs)
    print('ddd:')
    return Response(json.dumps(rs, ensure_ascii=False), content_type='application/json;charset=utf-8')
    # return jsonify(name='wwj')


@app.route('/post_r', methods=['GET', 'POST'])
def post_r():
    p_title = request.form.get('p_title')
    p_content = request.form.get('p_content')
    p_datetime = datetime.now()
    ps = db.getUserPasswd('wwj')
    print(ps)
    rs = db.addPost(p_title, p_content, p_datetime)
    print(p_title)
    print(p_content)
    # return Response('success')
    return render_template('msg.html', msg='发表成功')


@app.route('/login_r', methods=['post'])
def login_r():
    username = request.form.get('username')
    password = request.form.get('password')
    # print('{}{}'.format(username,password))
    print(username)
    print(password)
    return render_template('my_inf.html')


@app.route('/post_h')
def post_h():
    LoginUser = session.get('LoginUser')
    if LoginUser:
        print('用户登录了')
        print(LoginUser['username'])
        return render_template('post.html',LoginUser=LoginUser)
    else:
        print('用户未登录')
        return render_template('login.html')



@app.route('/post_page')
def post_page():
    page = request.args.get("page")
    rs = db.getPost((int(page) - 1) * 3, 3)
    print(rs)
    pages = db.getPostCount()
    f = pages % 3
    if f == 0:
        pages = pages // 3
    else:
        pages = pages // 3 + 1

    return render_template('list_post.html', page_num=int(page), post_list=rs, pages=pages + 1)


@app.route('/upload_image', methods=['post'])
def upload_image():
    msg = {
        "code": 0
        , "msg": "success"
        , "data": {
            "src": "/static/images"
            , "title": "a"
        }
    }
    return Response(json.dumps(msg), content_type='application/json')


@app.route('/subian')
def subian():
    # return jsonify(name='wwj')
    return Response('wwj')

init(app)

manager = Manager(app=app)
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(
    host='0.0.0.0'
))


if __name__ == '__main__':
    # app.run(host='0.0.0.0')
    manager.run()
