from flask import Flask, abort, url_for, redirect, session, flash
from flask import render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import DataRequired
from datetime import date
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

class NameForm(FlaskForm):
    name = StringField("What is your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")

class DateForm(FlaskForm):
    date = DateField("What is your date of birth?", format='%Y/%m/%d', validators=[DataRequired()])
    submit = SubmitField("Submit")

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = "Keep it a secret, at all costs"
app.config['SQLALCHEMY_DATABASE_URI'] = \
    f'sqlite:///{os.path.join(basedir, "data-dev.sqlite")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db =SQLAlchemy(app)

bootstrap = Bootstrap(app)

migrate = Migrate(app, db, render_as_batch=True)

@app.shell_context_processor ##Automatically adds new entries to your database
def make_shell_context():
    return dict(db=db, User=User, Role=Role)

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')
    def __repr__(self):
        return f"<Role {self.name}>"

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    ##age = db.Column(db.Integer)
    def __repr__(self):
        return f"<User {self.username}>"


#@app.route('/')
#def index():
#    return "Hello Web World!"

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        name_entered = form.name.data
        user = User.query.filter_by(username=name_entered).first()
        if user is None:
            user = User(username=name_entered)
            db.sesion.add(user)
            db.session.commit()
            session['known'] = False
        else:
            session['known'] = True
        session['name']= name_entered
        flash('Great! We hope you enjoy the community')
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'), known=session.get('known', False))

@app.route('/zodiac', methods=['GET', 'POST'])
def zodiac():
    form = DateForm()
    if form.validate_on_submit():
        session['date']= form.date.data
        if date.month == '12':
            astro_sign = 'Sagittarius' if (date.day < 22) else 'capricorn'
            flash("Welcome! {astro_sign}")
        elif date.month == '01':
            astro_sign = 'Capricorn' if (date.day < 20) else 'aquarius'
            flash("Welcome! {astro_sign}")
        elif date.month == '02':
            astro_sign = 'Aquarius' if (date.day < 19) else 'pisces'
            flash("Welcome! {astro_sign}")
        elif date.month == '03':
            astro_sign = 'Pisces' if (date.day < 21) else 'aries'
            flash("Welcome! {astro_sign}")
        elif date.month == '04':
            astro_sign = 'Aries' if (date.day < 20) else 'taurus'
            flash("Welcome! {astro_sign}")
        elif date.month == '05':
            astro_sign = 'Taurus' if (date.day < 21) else 'gemini'
            flash("Welcome! {astro_sign}")
        elif date.month == '06':
            astro_sign = 'Gemini' if (date.day < 21) else 'cancer'
            flash("Welcome! {astro_sign}")
        elif date.month == '07':
            astro_sign = 'Cancer' if (date.day < 23) else 'leo'
            flash("Welcome! {astro_sign}")
        elif date.month == '08':
            astro_sign = 'Leo' if (date.day < 23) else 'virgo'
            flash("Welcome! {astro_sign}")
        elif date.month == '09':
            astro_sign = 'Virgo' if (date.day < 23) else 'libra'
            flash("Welcome! {astro_sign}")
        elif date.month == '10':
            astro_sign = 'Libra' if (date.day < 23) else 'scorpio'
            flash("Welcome! {astro_sign}")
        elif date.month == '11':
            astro_sign = 'scorpio' if (date.day < 22) else 'sagittarius'
            flash("Welcome! {astro_sign}")
    else:
        session['date'] = form.date.data
        return redirect(url_for('index'))
    return render_template('zodiac.html', form=form, date=session.get('date'))


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


@app.errorhandler(404)
def page_not_found(e):
    error_title = "Not found"
    error_msg = "That page doesn't exist"
    return render_template('error.html', error_title=error_title, error_msg=error_msg), 404

@app.route('/article/<id>')
def article(id):
    article_text = article_loader(int(id))
    if not article_text:
        abort(404)
    return f"{article_text}"

def article_loader(id):
    if id == 1:
        return "Article about trucks"
    elif id == 2:
        return "Article about record players"
    else:
        return None

@app.errorhandler(500)
def internal_server_error(e):
    error_title = "Internal Server Error"
    error_msg = "Sorry, we seem to be experiencing some technical difficulties"
    return render_template('error.html',
                           error_title=error_title,
                           error_msg=error_msg), 500