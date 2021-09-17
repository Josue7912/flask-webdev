from flask import session, render_template, redirect, url_for, flash, request
from . import auth

from . forms import SignUpForm, SignInForm
from .. import db
from .. models import User, Post

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


@auth.route('/signin', methods=['GET', 'POST'])
def signin():
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


@auth.route('/logout')
def logout():
    session.clear()
    session['user_available'] = False
    return redirect(url_for('.index'))


if __name__ == '__main__':
    auth.run()