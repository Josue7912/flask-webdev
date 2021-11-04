from flask import session, render_template, redirect, url_for, flash, current_app, request
from . import main
from .forms import NameForm, EditProfileForm, AdminLevelEditProfileForm, CompositionForm
from .. import db
from ..models import Role, User
from flask_login import login_required, current_user
from ..models import Permission, Role, User, Composition
from ..decorators import admin_required, permission_required

@main.route('/admin')
@login_required
@admin_required
def for_admins_only():
    return "Welcome, Administrator!"

@main.route('/moderate')
@login_required
@permission_required(Permission.MODERATE)
def for_moderators_only():
    return "Greetings, Moderator!"

@main.route('/', methods=['GET', 'POST'])
def index():
    form = CompositionForm()
    if current_user.can(Permission.PUBLISH) \
            and form.validate_on_submit():
        composition = Composition(
            release_type=form.release_type.data,
            title=form.title.data,
            description=form.description.data,
            artist=current_user._get_current_object())
        db.session.add(composition)
        db.session.commit()
        composition.generate_slug()
        return redirect(url_for('.index'))
    page = request.args.get('page', 1, type=int)
    pagination = \
        Composition.query.order_by(Composition.timestamp.desc()).paginate(
            page,
            per_page=current_app.config['RAGTIME_COMPS_PER_PAGE'],
            error_out=False)
    compositions = pagination.items
    return render_template(
        'index.html',
        form=form,
        compositions=compositions,
        pagination=pagination
    )


#form = NameForm()
#if form.validate_on_submit():
#    name_entered = form.name.data
#    user = User.query.filter_by(username=name_entered).first()
#    if user is None:
#        user = User(username=name_entered)
#        db.session.add(user)
#        db.session.commit()
#        session['known'] = False
#    else:
#        session['known'] = True
#    session['name'] = name_entered
#    flash('Great! We hope you enjoy the community')
#    return redirect(url_for('.index'))
#return render_template('index.html', form=form, name=session.get('name'), known=session.get('known', False))

@main.route('/top-secret')
@login_required
def top_secret():
    return "Welcome, VIP member!"

@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', '_compositions.html', user=user)

@main.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.bio = form.bio.data
        db.session.add(current_user._get_current_object())
        db.session.commit()
        flash('You successfully updated your profile! Looks great.')
        return redirect(url_for('.user', username=current_user.username))
    form.name.data = current_user.name
    form.location.data = current_user.location
    form.bio.data = current_user.bio
    return render_template('edit_profile.html', form=form)

@main.route('/editprofile/<int:id>', methods=['GET', 'POST'])
@admin_required
def admin_edit_profile():
    form = AdminLevelEditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.location = form.location.data
        current_user.role = form.role.data
        current_user.location = form.location.data
        current_user.bio = form.bio.data
        db.session.add(current_user._get_current_object())
        db.session.commit()
        flash('You successfully updated your profile! Looks great.')
        return redirect(url_for('.user', username=current_user.username))
    form.username.data = current_user.username
    form.location.data = current_user.location
    form.role.data = current_user.role
    form.location.data = current_user.location
    form.bio.data = current_user.bio
    return render_template('edit_profile.html', form=form)

@main.route('/edit-profile-admin/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_profile_admin(id):
    user = User.query.get_or_404(id)
    form = EditProfileAdminForm(user=user)
    if form.validate_on_submit():
        user.email = form.email.data
        user.username = form.username.data
        user.confirmed = form.confirmed.data
        user.role = Role.query.get(form.role.data)
        user.location = form.location.data
        user.bio = form.bio.data
        db.session.add(current_user._get_current_object())
        db.session.commit()
        flash('The profile was updated.')
        return redirect(url_for('.user', username=user.username))
    form.email.data = user.email
    form.username.data = user.username
    form.confirmed.data = user.confirmed
    form.role.data = user.role_id
    form.name.data = user.name
    form.location.data = user.location
    form.bio.data = user.bio
    return render_template('edit_profile.html', form=form, user=user)


@main.route('/composition/<slug>')
def composition(slug):
    composition = Composition.query.filter_by(slug=slug).first_or_404()
    return render_template('composition.html', compositions=[composition])