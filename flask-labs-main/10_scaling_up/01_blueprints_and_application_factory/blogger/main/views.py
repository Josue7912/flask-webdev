from flask import session, render_template, redirect, url_for, flash, request
from . import main

from . forms import AboutUserForm
from .. import db
from .. models import User, Post

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/about_user')
def about_user():
    aboutuserform = AboutUserForm()
    if session['user_available']:
        user = User.query.filter_by(username=session['current_user']).first()
        return render_template('about_user.html', user=user, aboutuserform=aboutuserform)
    flash('You are not a Authenticated User')
    return redirect(url_for('.index'))


if __name__ == '__main__':
    main.run()