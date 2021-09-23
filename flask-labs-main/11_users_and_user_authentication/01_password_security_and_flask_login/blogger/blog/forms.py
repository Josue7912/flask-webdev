from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, SubmitField, PasswordField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, Email, ValidationError

def length_check(form,field):
    if len(field.data) == 0:
        raise ValidationError('Fields should not be null')

class AddPostForm(FlaskForm):
    title = TextField('Title', validators=[ DataRequired()])
    description = TextAreaField('Description', validators = [DataRequired()])