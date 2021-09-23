from operator import length_hint
from flask.app import Flask
from flask_wtf import FlaskForm
from wtforms.fields.core import BooleanField, StringField
from wtforms import SubmitField
from wtforms.fields.simple import PasswordField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from wtforms.validators import Regexp, EqualTo
from ..models import User


def length_check(form,field):
    if len(field.data) == 0:
        raise ValidationError('Fields should not be null')


class LoginForm(FlaskForm):
    email = StringField('Email', validators= [DataRequired(), length_check, Email()])
    password = PasswordField('Password', validators=[ DataRequired(), Length(min=6)])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField("Log In")

class RegistrationForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(),
                                    Length(1,64),
                                    Email()])
    username = StringField('Username', validators=[
        DataRequired(),
        Length(1, 64),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                   'Usernames must have only letters, numbers, dots, or underscores',
        )])
    password = PasswordField('Password', validators=[
        DataRequired(),
        EqualTo('password_confirm', message='Passwords do not match.'
        )])
    password_confirm = PasswordField('Password (confirm):',
                                     validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Sorry! Username already in use.')