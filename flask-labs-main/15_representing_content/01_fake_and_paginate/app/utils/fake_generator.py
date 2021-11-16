from re import U
from sqlalchemy.exc import IntegrityError
from faker import Faker
from random import randint
import string
from app.models import User, TodoList, Todo
from app import db

def users(count=10):
    fake = Faker()
    i = 0
    while i < count:
        u = User(
            username=fake.user_name(),
            email=fake.email(),
            password='password',
            member_since=fake.past_date(),
            last_seen=fake.past_date())
        db.session.add(u)
        try:
            db.session.commit()
            i += 1
        except IntegrityError:
            db.session.rollback()


def todolists(count=75):
    fake = Faker()
    user_count = User.query.count()
    for i in range(count):
        u = User.query.offset(randint(0, user_count - 1)).first()
        t = TodoList(
            title=string.capwords(fake.bs()),
            created_at=fake.past_date(),
            creator=u
        )
        db.session.add(t)
    db.session.commit()


def todos():
    fake = Faker()
    user_count = User.query.count()
    for i in range(10):
        u = User.query.offset(randint(0, user_count - 1)).first()
        t = TodoList.query.filter_by(creator=u).offset(randint(0, todolists -1)).first()
        for k in range(randint(5, 75)):
            tk = Todo(
                description=fake.text(),
                created_at=fake.past_date(),
                finished_at=fake.past_date(),
                is_finished=string.capwords(fake.text()),
                creator=u,
                todolist = t
            )
            db.session.add(tk)
    db.session.commit()