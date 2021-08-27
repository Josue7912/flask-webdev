"""
"""
from flask_reddit.threads import constants as THREAD
from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField
from wtforms.validators import Required, URL, Length

class SubmitForm(FlaskForm):
    name = TextField('Name your community!', [Required()])
    desc = TextAreaField('Description of subreddit!', [Required()])
