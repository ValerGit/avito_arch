from flask import Flask, request
import requests
import json
import os
app = Flask(__name__)
f = open('api_conf.json', 'r')
js = json.load(f)
api = js["key"]


@app.route('/<string:mode>/')
def weather_c(mode):
    city = request.args.get('city')
    dtReq = request.args.get('dt')
    if city and mode:
        if mode == 'current':
            r = requests.get(
                'http://api.openweathermap.org/data/2.5/weather?q=%s&units=metric&APPID=%s' %
                (city, api))
            resp = r.json()
            return "City: %s, unit: celsius, temperature: %s, weather: %s" % (
                resp["name"], resp["main"].get("temp"), resp["weather"][0]["main"])
        elif mode == 'forecast' and dtReq:
            r = requests.get(
                'http://api.openweathermap.org/data/2.5/forecast?q=%s&units=metric&APPID=%s' %
                (city, api))
            resp = r.json()
            app.logger.info(resp["list"][0]["dt"])
            dt = int(dtReq)
            for i in resp["list"]:
                if (i["dt"] == dt):
                    return i
                return 'dt not found'
        else:
            return 'wrong mode or dt'
    else:
        return 'wrong url'


if __name__ == '__main__':
    if os.getenv('PORT'):
        app.run(debug=True, port=os.getenv('PORT'))
    else:
        app.run(debug=True, port=5000, host='0.0.0.0')
