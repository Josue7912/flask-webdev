import re
from . import db, login_manager
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin, AnonymousUserMixin
from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from datetime import datetime
import hashlib
import bleach

class Permission:
    FOLLOW = 1
    REVIEW = 2
    PUBLISH = 4
    MODERATE = 8
    ADMIN = 16

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.permissions is None:
            self.permissions = 0

    def __repr__(self):
        return f"<Role {self.name}>"

    @staticmethod
    def insert_roles():
        roles = {
            'User':             [Permission.FOLLOW,
                                 Permission.REVIEW,
                                 Permission.PUBLISH],
            'Moderator':        [Permission.FOLLOW,
                                 Permission.REVIEW,
                                 Permission.PUBLISH,
                                 Permission.MODERATE],
            'Administrator':    [Permission.FOLLOW,
                                 Permission.REVIEW,
                                 Permission.PUBLISH,
                                 Permission.MODERATE,
                                 Permission.ADMIN],
        }
        default_role = 'User'
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.reset_permissions()
            for perm in roles[r]:
                role.add_permission(perm)
            role.default = (role.name == default_role)
            db.session.add(role)
        db.session.commit()

    def add_permission(self, perm):
        if not self.has_permission(perm):
            self.permissions += perm

    def remove_permission(self, perm):
        if self.has_permission(perm):
            self.permissions -= perm

    def reset_permissions(self):
        self.permissions = 0

    def has_permission(self, perm):
        return self.permissions & perm == perm

class Follow(db.Model):
    __tablename__ = 'follows'

    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    following_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(64), unique=True, index=True)
    confirmed = db.Column(db.Boolean, default=False)
    name = db.Column(db.String(64))
    location = db.Column(db.String(64))
    bio = db.Column(db.Text())
    last_seen = db.Column(db.DateTime(), default=datetime.utcnow)
    compositions = db.relationship('Composition', backref='artist', lazy='dynamic')

    following = db.relationship(
        'Follow',
        foreign_keys=[Follow.follower_id],
        backref=db.backref('follower', lazy='joined'),
        lazy ='dynamic',
        cascade='all, delete-orphan')

    followers = db.relationship(
        'Follow',
        foreign_keys=[Follow.following_id],
        backref=db.backref('following', lazy='joined'),
        lazy ='dynamic',
        cascade='all, delete-orphan')


    avatar_hash = db.Column(db.String(32))
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.role is None:
            if self.email == current_app.config['RAGTIME_ADMIN']:
                self.role = Role.query.filter_by(name='Administrator').first()
            if self.role is None:
                self.role = Role.query.filter_by(default=True).first()
            if self.email is not None and self.avatar_hash is None:
                self.avatar_hash = self.email_hash()

    def email_hash(self):
        return hashlib.md5(self.email.lower().encode('utf-8')).hexdigest()

    def unicornify(self, size=128):
        url = 'https://unicornify.pictures/avatar'
        hash = self.avatar_hash or self.email_hash()
        return f'{url}/{hash}?s={size}'

    def __repr__(self):
        return f"<User {self.username}>"

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_confirmation_token(self, expiration_sec=3600):
        s = Serializer(current_app.secret_key, expiration_sec)
        return s.dumps({'confirm_id': self.id}).decode('utf-8')

    def confirm(self, token):
        s = Serializer(current_app.secret_key)
        try:
            data = s.loads(token.encode('utf-8'))
        except:
            return False
        if data.get('confirm.id') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True

    def can(self, perm):
        return self.role is not None and self.role.has_permission(perm)

    def is_administrator(self):
        return self.can(Permission.ADMIN)

    def ping(self):
        self.last_seen = datetime.utcnow()
        db.session.add(self)
        db.session.commit()

    def follow(self, user):
        if not self.is_following(user):
            f = Follow(follower=self, following=user)
            db.session.add(f)

    def unfollow(self, user):
        f = self.following.filter_by(following_id=user.id).first()
        if f:
            db.session.delete(f)

    def is_following(self, user):
        if user.id is None:
            return False
        return self.following.filter_by(
            following_id=user.id).first() is not None

    def is_a_follower(self, user):
        if user.id is None:
            return False
        return self.followers.filter_by(
            follower_id=user.id).first() is not None


class AnonymousUser(AnonymousUserMixin):
    def can(self, perm):
        return False

    def is_administrator(self):
        return False

login_manager.anonymous_user = AnonymousUser

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class ReleaseType:
    SINGLE = 1
    EXTENDED_PLAY = 2
    ALBUM = 3

class Composition(db.Model):
    __tablename__ = 'compositions'
    id = db.Column(db.Integer, primary_key=True)
    release_type = db.Column(db.Integer)
    title = db.Column(db.String(64))
    description = db.Column(db.Text)
    timestamp = db.Column(db.DateTime,
        index=True, default=datetime.utcnow)
    artist_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    description_html = db.Column(db.Text)
    slug = db.Column(db.String(128), unique=True)

    @staticmethod
    def on_changed_description(target, value, oldvalue, initiator):
        allowed_tags = ['a']
        html = bleach.linkify(bleach.clean(value,
                                           tags=allowed_tags,
                                           strip=True))
        target.description_html = html

    def generate_slug(self):
        self.slug = f"{self.id}-" + re.sub(r'[^\w]+', '-', self.title.lower())
        db.session.add(self)
        db.session.commit()

db.event.listen(Composition.description,
                'set',
                Composition.on_changed_description)