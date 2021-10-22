from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, TextAreaField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError, Regexp
from ..models import User

class NameForm(FlaskForm):
    name = StringField("What is your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")

class EditProfileForm(FlaskForm):
    name = StringField("Name", validators=[Length(0, 64)])
    location = StringField("Location", validators=[Length(0,64)])
    bio = TextAreaField("Bio")
    submit = SubmitField("Submit")

class AdminLevelEditProfileForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(),
        Length(1, 64),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                   'Usernames must have only letters, numbers, dots, or underscores',
        )])
    confirmed = BooleanField('Keep me logged in')
    role = SelectField('Roles', choices=[(1, "User"), (2, "Moderator"), (3, "Admin")], coerce=int)
    location = StringField("Location", validators=[Length(0,64)])
    bio = TextAreaField("Bio")

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Sorry! Username already in use.')