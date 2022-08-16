from flask import Flask, jsonify, render_template
import pymongo
import urllib.parse
import requests
#import json
from pymongo import MongoClient

app = Flask(__name__)

def get_db():
    client = MongoClient(host='test_mongodb',
                         port=27017, 
                         username='root', 
                         password='pass',
                        authSource="admin")
    db = client["place"]
    return db

@app.route('/')
def ping_server():
    return "Welcome to the world of animals."

api_key = '687168615a74657337377378686a76'
@app.route('/data_request')
def request_test():
    response = requests.get(f"http://openapi.seoul.go.kr:8088/{api_key}/json/LOCALDATA_072404_YD/1/5/")
    result = response.json()

    db = get_db()
    print(db)
    #db.place.insertMany(result['LOCALDATA_072404_YD']['row'] )
    return result['LOCALDATA_072404_YD']

@app.route('/animals')
def get_stored_animals():
    db = get_db()
    _animals = db.animal_tb.find()
    animals = [{"id": animal["id"], "name": animal["name"], "type": animal["type"]} for animal in _animals]
    return jsonify({"animals": animals})

@app.route('/test')
def test_server():
    return "this is thest"

@app.route('/other_test')
def test_server2():
    return "other test"

@app.route('/abc')
def test_server3():
    return "oter test2"

@app.route('/etf')
def test_server4():
    headers = {
    'X-NCP-APIGW-API-KEY-ID': 'alkr8hxm7f',
    'X-NCP-APIGW-API-KEY': 'qbYyrkjNAkiRyk523Ti75ugWKbf7mN2ETZQXh9kO',
    }

    data = {
        'query': '서울특별시 영등포구 선유동1로 4 (당산동2가)'
    }
    data = urllib.parse.urlencode(data)s
    result = requests.get("https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?", headers=headers, params=data)
    return result.json()

@app.route('/fff1')
def test_server5():
    return render_template('./html_file.html')

if __name__=='__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)

    AIzaSyDL3xwAcv_0BN51C69DF7WeBzTkB5iUX3k