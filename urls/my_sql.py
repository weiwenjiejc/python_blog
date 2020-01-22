# -*- coding: utf-8 -*-
from flask import Blueprint

from ext import db

wsql = Blueprint('wsql', __name__)


@wsql.route('/create')
def create():


    db.create_all()
    return 'ok'
