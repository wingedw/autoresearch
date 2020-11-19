from flask import Flask
from flask_restful import Resource, Api
#from flask_cors import CORS
import requests
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

app = Flask(__name__)
api = Api(app)
#CORS(app) ## To a low direct AJAX calls
 
@app.route('/year', methods=['GET'])
def Get():
    uri= environ.get('YEARS')
    r = requests.get(uri)
    return r.json()

@app.route('/make/<year>', methods=['GET'])
def GetMakes(year):
    uri= environ.get('MAKES')
    r = requests.get(uri.format(year))
    return r.json()

@app.route('/model/<year>/<make>', methods=['GET'])
def GetModel(year,make):
    uri = environ.get('MODELS')
    r = requests.get(uri.format(year,make))
    return r.json()

@app.route('/report/<year>/<make>/<model>', methods=['GET'])
def GetReport(year,make,model):
    uri = environ.get('REPORT')
    r = requests.get(uri.format(year,make,model))
    return r.json()


if __name__ == '__main__':
   app.run(debug = True, port=80)