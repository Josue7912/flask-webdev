from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, SubmitField, PasswordField, BooleanField, StringField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, Email, ValidationError

def length_check(form,field):
    if len(field.data) == 0:
        raise ValidationError('Fields should not be null')


class SignUpForm(FlaskForm):
    firstname= TextField('First Name', validators= [DataRequired(), length_check])
    lastname = TextField('Last Name', validators= [DataRequired()])
    username = TextField('User Name', validators= [ DataRequired(), Length(min=4)])
    password = PasswordField('Password',validators=[ DataRequired(), Length(min=6)])
    email = EmailField('Email', validators= [DataRequired(), Email()])
    submit = SubmitField('Sign Up')


class SignInForm(FlaskForm):
    email = EmailField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired(), Length(min=6, max=30)])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Sign In')
