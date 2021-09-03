from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)


#@app.route('/')
#def index():
#    return "Hello Web World!"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<username>')
def user(username):
    return render_template('user.html', username=username)

@app.route('/about')
def about():
    return "<p>I hope to understand how to build apps that helps me to automate with applications some daily workloads</p>"

#@app.route('/songs')
#def songs():
#    return "<li>Tiroteo</li>"\
#        "<li>Todo de Ti</li>"\
#        "<li>Millones</li>"

@app.route('/songs')
def songs():
    songs = ["Millones", "Todo de Ti", "Tiroteo", "Somewhere I Belong"]
    return render_template('songs.html', favourite_songs=songs)

@app.route('/back')
def back():
    return "<a href=songs>Songs</a>"\
        "<a href=about>About me</a>"


##@app.route('/user/<username><age>')
##def user(username,age):
##    return f"Hello {username}{age}!"

@app.route('/maths/<number>')
def maths(number):
    x = number
    print(x)
    y = int(x)**2
    return str(y)