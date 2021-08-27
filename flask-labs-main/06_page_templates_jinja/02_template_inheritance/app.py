from flask import Flask

app = Flask(__name__)


@app.route('/')
def welcome():
    return "Welcome to Emily's Dog Costumes! See my <a href=\"/services\">services</a> and current line of <a href=\"/costumes\">costumes</a>"


@app.route('/services')
def services():
    return "I offer custom made costumes for your precious canine companion, "\
        "and a free in-home consultation, to get the measurements."


@app.route('/costumes')
def costumes():
    return "Check out my costumes!"
