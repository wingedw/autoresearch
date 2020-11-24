from flask import Flask
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from flask_restplus import Api, Resource, fields
import requests
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

app = Flask(__name__)
api = Api(app, version='0.1', title='CQ API',
    description='Car Query Specs API',
)

ns = api.namespace('cq', description='CQ APIs')

class CQClass(object):
    
    def __init__(self):
        self.counter = 0

if __name__ == '__main__':
   app.run(debug = True, port=80)