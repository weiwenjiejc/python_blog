# -*- coding: utf-8 -*-
from flask import Blueprint, render_template

whtml = Blueprint('whtml', __name__)


@whtml.route('/html/login')
def login():
    return render_template('login.html')

@whtml.route('/html/register')
def register():
    return render_template('register.html')
