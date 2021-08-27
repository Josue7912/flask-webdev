"""
"""
from flask_reddit.threads import constants as THREAD
from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField
from wtforms.validators import Required, URL, Length

class SubmitForm(FlaskForm):
    title = TextField('Title', [Required()])
    text = TextAreaField('Body text') # [Length(min=5, max=THREAD.MAX_BODY)]
    link = TextField('Link', [URL(require_tld=True,
        message="That is not a valid link url!")])
