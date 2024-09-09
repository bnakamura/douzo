from distutils.log import Log
from flask import Flask, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from flask_mail import Mail

import importlib
import logging
import os
from datetime import timedelta

# blue printで作る
app = Flask(
    __name__,
    static_folder = "views/static",
    template_folder = "views/templates"
)

db = SQLAlchemy()
mail = Mail()
csrf = CSRFProtect()

class Config:

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{dbname}?charset=utf8'.format(**{
        'user': os.getenv('MYSQL_USER', ''),
        'password': os.getenv('MYSQL_PASSWORD', ''),
        'host': 'mysql_koz',
        'dbname': 'hoge'
    })


    # Assets Management
    ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static/assets') 

    # セッションを使う際の秘密キー
    SECRET_KEY = os.getenv('SECRET_KEY', '') 

    # CSRFトークンの設定
    WTF_CSRF_SECRET_KEY = os.getenv('CSRF_SECRET', '')
    
    # session 
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)

    WTF_CSRF_ENABLED = True

    # jsonをそのままダンプする(ASCIIにしない)
    JSON_AS_ASCII = False

    # Gmail Setting
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS =  True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME', '')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', '')
    MAIL_DEFAULT_SENDER = 'FLASK-SAMPLE'

def create_app():

    # blue printでルートを設定する
    from apps.pymodule.landing import index as landing_view
    app.register_blueprint(landing_view.landing)

    return app

@app.errorhandler(500)
def error_500(e):
    print('httpステータス:{}, メッセージ:{}, 詳細:{}'.format(e.code, e.name, e.description))
    return jsonify({'message': 'internal server error', 'action': 'サーバエラーが発生しました。しばらくしてからもう一度アクセスしてください。'}), 500

@app.errorhandler(404)
def error_404(e):
    print('httpステータス:{}, メッセージ:{}, 詳細:{}'.format(e.code, e.name, e.description))
    return jsonify({'message': 'ページが存在しないようです。URLをもう一度ご確認ください', 'action': 'ページが存在しないようです。URLをもう一度ご確認ください'}), 404