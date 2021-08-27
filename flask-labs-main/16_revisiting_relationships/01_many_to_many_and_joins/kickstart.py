"""
This helper script instantiates critical components of our webapps.
We need at least one home subreddit to get things going.
We also need a first user to admin our first subreddit.
"""
import os
import sys
import readline

from werkzeug.security import check_password_hash, generate_password_hash

from flask_reddit import db
from flask_reddit.users.models import User
from flask_reddit.subreddits.models import Subreddit

db.drop_all()
db.create_all()

first_user = User(username='root', email='root@example.com', \
        password=generate_password_hash('347895237408927419471483204721'))

#db.session.add(first_user)
db.session.commit()

first_subreddit = Subreddit(name='frontpage', desc='Welcome to Reddit! Here is our homepage.',
        admin_id=first_user.id)

db.session.add(first_subreddit)
db.session.commit()
