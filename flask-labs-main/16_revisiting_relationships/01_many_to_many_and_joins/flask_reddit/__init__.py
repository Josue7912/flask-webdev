#!/usr/bin/env python
"""
"""
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.routing import BaseConverter


app = Flask(__name__, static_url_path='/static')
app.config.from_object('config')

db = SQLAlchemy(app)

class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]

app.url_map.converters['regex'] = RegexConverter

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500

@app.shell_context_processor
def context_processor():
    from flask_reddit.users.models import User
    from flask_reddit.threads.models import Thread, thread_upvotes
    from flask_reddit.subreddits.models import Subreddit
    return dict(User=User, Thread=Thread, Subreddit=Subreddit,
        thread_upvotes=thread_upvotes)

from flask_reddit.users.views import mod as users_module
app.register_blueprint(users_module)

from flask_reddit.threads.views import mod as threads_module
app.register_blueprint(threads_module)

from flask_reddit.frontends.views import mod as frontends_module
app.register_blueprint(frontends_module)

from flask_reddit.apis.views import mod as apis_module
app.register_blueprint(apis_module)

from flask_reddit.subreddits.views import mod as subreddits_module
app.register_blueprint(subreddits_module)

def custom_render(template, *args, **kwargs):
    """
    custom template rendering including some flask_reddit vars
    """
    return render_template(template, *args, **kwargs)

app.debug = app.config['DEBUG']

if __name__ == '__main__':
    print('We are running flask via main()')
    app.run()
