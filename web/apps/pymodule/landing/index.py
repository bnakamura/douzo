from flask import Blueprint,request
from apps.app import db, app

landing = Blueprint('landing', 
        __name__, 
        url_prefix='/')

@landing.route('/')
def index():
        print(request.headers)
        return "hello world"
