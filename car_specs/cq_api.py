from flask import Flask
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from flask_restplus import Api, Resource, fields
import requests
import json
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

app = Flask(__name__)
api = Api(app, version='0.1', title='CQ API',
    description='Car Query Specs API',
)

ns = api.namespace('cq', description='CQ APIs')

class CQ_Class(object):
    
    def __init__(self):
        self.counter = 0

    def GetYears(self):
        uri= environ.get('CQ_YEARS')
        r = requests.get(uri)
        result = r.json #.replace('?','',1)
        #result = json.dumps(result)
        #result = result.replace('?','',1)
        d = json.loads('{ "Years": {"min_year":"1941", "max_year":"2019"} }')
        data = "bob"
        return data

GetJason = CQ_Class()

@ns.route('/year')
class YearJson(Resource):

    @ns.doc('Model Years Range')
    def get(self):
       return GetJason.GetYears()

if __name__ == '__main__':
   app.run(debug = True, port=5050)