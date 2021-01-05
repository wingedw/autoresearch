class Endpoint:
    year = "https://webapi.nhtsa.gov/api/SafetyRatings?format=json"
    make = "https://webapi.nhtsa.gov/api/SafetyRatings/modelyear/{0}?format=json"
    model = "https://webapi.nhtsa.gov/api/SafetyRatings/modelyear/{0}/make/{1}?format=json"
    report = "https://one.nhtsa.gov/webapi/api/Recalls/vehicle/modelyear/{0}/make/{1}/model/{2}?format=json"
