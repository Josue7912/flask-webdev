from flask import session, render_template, redirect, url_for, flash
from . import main
from .forms import NameForm
from .. import db
from ..models import Role, User
from flask_login import login_required

@main.route('/', methods=['GET', 'POST'])
def index():
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
    return render_template('index.html', form=form, name=session.get('name'), known=session.get('name'))

@main.route('/top-secret')
@login_required
def top_secret():
    return "Welcome, VIP member!"