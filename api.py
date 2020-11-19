from flask import Flask
from flask_restful import Resource, Api
#from flask_cors import CORS
import requests
 
app = Flask(__name__)
api = Api(app)
#CORS(app) ## To allow direct AJAX calls
 
@app.route('/year', methods=['GET'])
def Get():
    uri='https://webapi.nhtsa.gov/api/SafetyRatings?format=json'
    r = requests.get(uri)
    return r.json()

@app.route('/make/<year>', methods=['GET'])
def GetMakes(year):
    uri='https://webapi.nhtsa.gov/api/SafetyRatings/modelyear/{0}?format=json'
    r = requests.get(uri.format(year))
    return r.json()

@app.route('/model/<year>/<make>', methods=['GET'])
def GetModel(year,make):
    uri='https://webapi.nhtsa.gov/api/SafetyRatings/modelyear/{0}/make/{1}?format=json'
    r = requests.get(uri.format(year,make))
    return r.json()

@app.route('/report/<year>/<make>/<model>', methods=['GET'])
def GetReport(year,make,model):
    uri='https://one.nhtsa.gov/webapi/api/Recalls/vehicle/modelyear/{0}/make/{1}/model/{2}?format=json'
    r = requests.get(uri.format(year,make,model))
    return r.json()


if __name__ == '__main__':
   app.run(debug = True, port=80)