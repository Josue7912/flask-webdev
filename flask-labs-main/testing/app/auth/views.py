from flask import session, render_template, redirect, url_for, flash
from . import main

from .forms import NameForm
from .. import db
from ..models import Role, User

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = NameForm()
    if form.validate_on_submit():
        name_entered = form.name.data
        user = User.query.filter_by(username=name)
        if user is None:
            user = User(username=name_entered)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = name_entered
        flash('Great! We hope you enjoy the community')
        return redirect(url_for('.index'))
    return render_template('login.html', form=form, name=session.get('name'), known=session.get('name'))

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = NameForm()
    if form.validate_on_submit():
        name_entered = form.name.data
        user = User.query.filter_by(username=name)
        if user is None:
            user = User(username=name_entered)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = name_entered
        flash('Great! We hope you enjoy the community')
        return redirect(url_for('.index'))
    return render_template('register.html', form=form, name=session.get('name'), known=session.get('name'))