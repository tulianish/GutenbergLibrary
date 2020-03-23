import requests
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def Home():
    return render_template('home.html',shownotes='false')


@app.route('/submit', methods=['POST'])
def MainHandler():
    keyword = request.form['keyword']
    print(keyword)
    logFlag = requests.get("http://127.0.0.1:5001/logs/" + keyword)
    CatalogueService = requests.get("http://127.0.0.1:5002/catalogue/" + keyword)

    if CatalogueService.text == '0':
        showtable = 'false'
        shownotes = 'false'
    else:
        showtable = 'true'
        shownotes='true'
    return render_template('home.html', showtable=showtable, test=CatalogueService.json(), shownotes=shownotes,
                           keyword=keyword)
