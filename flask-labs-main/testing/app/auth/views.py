from flask import render_template, flash, redirect, url_for, request, session
from . import auth
from .. import db
from .forms import LoginForm, RegistrationForm
from .. models import User
from flask_login import login_user, logout_user


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email_entered = form.email.data
        user = User.query.filter_by(email=email_entered).first()
        if user is None:
            user = User(email=email_entered)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
        else:
            login_user(user, form.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.index')
            return redirect(next)
        flash('The username/password is invalid')
    return render_template('auth/login.html', form=form)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        name_entered = form.user.data
        user = User.query.filter_by(username=name_entered).first()
        if user is None:
            user = User(username=name_entered)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = name_entered
        flash('Great! Now you can log in to the website')
        return redirect(url_for('.index'))
    return render_template('auth/register.html', form=form)

@auth.route('/logout')
def logout():
    logout_user()
    flash("You've been logged out successfully")
    return redirect(url_for('main.index'))