from flask import Flask, request, render_template
import requests, json

app = Flask(__name__)
f = open('api_conf.json', 'r')
js = json.load(f)
api = js["key"]

@app.route('/<string:mode>/')
def weather_c(mode):
    city = request.args.get('city')
    dt = request.args.get('dt')
    if(mode == 'current'):
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=%s&units=metric&APPID=%s' % (city, api))
        resp = r.json()
        print (resp["weather"][0]["main"])
        return "City: %s, unit: celsius, temperature: %s, weather: %s" % (resp["name"], resp["main"].get("temp"), resp["weather"][0]["main"])

if __name__ == '__main__':
    app.run(debug=True, port=5000)