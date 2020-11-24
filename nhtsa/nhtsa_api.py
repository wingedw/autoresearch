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
api = Api(app, version='0.1', title='NHTSA API',
    description='National Highway Traffic Safety Administration Recall API',
)

ns = api.namespace('nhtsa', description='NHTSA APIs')

class NHTSAClass(object):
    
    def __init__(self):
        self.counter = 0

    def GetYears(self):
        uri= environ.get('YEARS')
        r = requests.get(uri)
        return r.json()
   
    def GetMakes(self, year):
        uri= environ.get('MAKES')
        r = requests.get(uri.format(year))
        return r.json()

    def GetModels(self, year, make):
        uri = environ.get('MODELS')
        r = requests.get(uri.format(year,make))
        return r.json()

    def GetReport(self, year, make, model):
        uri = environ.get('REPORT')
        r = requests.get(uri.format(year,make,model))
        return r.json()

GetJason = NHTSAClass()

@ns.route('/year')
class YearJson(Resource):

    @ns.doc('List of Years')
    def get(self):
       return GetJason.GetYears()

@ns.route('/make/<year>')
@ns.param('year', 'Model Year')
class MakeJson(Resource):

    @ns.doc('List of Makes')
    def get(self,year):
       return GetJason.GetMakes(year)

@ns.route('/model/<year>/<make>')
@ns.param('year', 'Model Year')
@ns.param('make', 'Auto Manufacture Name')
class ModelJson(Resource):

    @ns.doc('List of Models per Manufacturer')
    def get(self, year, make):
       return GetJason.GetModels(year, make)

@ns.route('/report/<year>/<make>/<model>')
@ns.param('year', 'Model Year')
@ns.param('make', 'Auto Manufacturer Name')
@ns.param('model', 'Model of Auto')
class ReportJson(Resource):

    @ns.doc('Recall Report')
    def get(self, year, make, model):
       return GetJason.GetReport(year, make, model)


if __name__ == '__main__':
   app.run(debug = True, port=80)