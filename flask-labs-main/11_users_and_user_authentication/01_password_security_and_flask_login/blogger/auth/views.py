from flask import session, render_template, redirect, url_for, flash, request
from . import auth

from . forms import SignUpForm, SignInForm
from .. import db
from .. models import User, Post
from flask_login import login_user, logout_user

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    signupform = SignUpForm(request.form)
    if request.method == 'POST':
        reg = User(signupform.firstname.data, signupform.lastname.data,\
         signupform.username.data, signupform.password.data,\
         signupform.email.data)
        db.session.add(reg)
        db.session.commit()
        return redirect(url_for('.index'))
    return render_template('signup.html', signupform=signupform)


##@auth.route('/signin', methods=['GET', 'POST'])
##def signin():
    signinform = SignInForm()
    if request.method == 'POST':
        em = signinform.email.data
        log = User.query.filter_by(email=em).first()
        if log.password == signinform.password.data:
            current_user = log.username
            session['current_user'] = current_user
            session['user_available'] = True
            return redirect(url_for('show_posts'))
    return render_template('signin.html', signinform=signinform)

@auth.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SignInForm()
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

@auth.route('/logout')
def logout():
    logout_user()
    flash("You've been logged out successfully")
    return redirect(url_for('main.index'))

##@auth.route('/logout')
##def logout():
    session.clear()
    session['user_available'] = False
    return redirect(url_for('.index'))


if __name__ == '__main__':
    auth.run()