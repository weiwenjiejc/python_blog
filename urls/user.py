from flask import Blueprint, Response

user = Blueprint('user', __name__)


@user.route('/login_r')
def login_r():
    # return Response('sdfdsf')
    return 'jslkdjf'
