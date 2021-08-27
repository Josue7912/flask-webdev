from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello Josué!"


@app.route('/about')
def about():
    return "<p>I hope to understand how to build apps that helps me to automate with applications some daily workloads</p>"


@app.route('/songs')
def songs():
    return "<li>Tiroteo</li>"\
        "<li>Todo de Ti</li>"\
        "<li>Millones</li>"

@app.route('/back')
def back():
    return "<a href={{url_for('songs')}}>Songs</a>"\
        "<a href={{url_for('about')}}>About me</a>"


@app.route('/user/<username><age>')
def user(username,age):
    return f"Hello {username}{age}!"

@app.route('/maths/<number>')
def maths(number):
    x = {number}
    y = x^2
    return y