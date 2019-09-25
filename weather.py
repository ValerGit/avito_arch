from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/<string:mode>/')
def weather_c(mode):
    city = request.args.get('city')
    return "%s weather for city %s" % (mode, city)

if __name__ == '__main__':
    app.run(debug=True, port=5000)