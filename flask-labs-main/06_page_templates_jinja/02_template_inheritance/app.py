from flask import Flask
from flask.templating import render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/costumes')
def costumes():
    return render_template('costumes.html')
