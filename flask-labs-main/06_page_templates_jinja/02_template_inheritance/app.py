from flask import Flask
from flask.templating import render_template

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/costumes')
def costumes():
    return render_template('costumes.html')
