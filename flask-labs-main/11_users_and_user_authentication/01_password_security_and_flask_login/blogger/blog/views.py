from flask import session, render_template, redirect, url_for, flash, request
from . import blog

from . forms import AddPostForm
from .. import db
from .. models import User, Post

@blog.route('/posts')
def show_posts():
    if session['user_available']:
        posts = Post.query.all()
        user = User.query.all()
        return render_template('posts.html', posts=posts, user=user)
    flash('User is not Authenticated')
    return redirect(url_for('.index'))


@blog.route('/add', methods=['GET', 'POST'])
def add_post():
    if session['user_available']:
        blogpost = AddPostForm(request.form)
        us = User.query.filter_by(username=session['current_user']).first()
        if request.method == 'POST':
            bp = Post(blogpost.title.data, blogpost.description.data, us.uid)
            db.session.add(bp)
            db.session.commit()
            return redirect(url_for('show_posts'))
        return render_template('add.html', blogpost=blogpost)
    flash('User is not Authenticated')
    return redirect(url_for('.index'))


@blog.route('/delete/<pid>/<post_owner>', methods=('GET', 'POST'))
def delete_post(pid, post_owner):
    if session['current_user'] == post_owner:
        me = Post.query.get(pid)
        db.session.delete(me)
        db.session.commit()
        return redirect(url_for('show_posts'))
    flash('You are not a valid user to Delete this Post')
    return redirect(url_for('show_posts'))


@blog.route('/update/<pid>/<post_owner>', methods=('GET', 'POST'))
def update_post(pid, post_owner):
    if session['current_user'] == post_owner:
        me = Post.query.get(pid)
        blogpost = AddPostForm(obj=me)
        if request.method == 'POST':
            bpost = Post.query.get(pid)
            bpost.title = blogpost.title.data
            bpost.description = blogpost.description.data
            db.session.commit()
            return redirect(url_for('show_posts'))
        return render_template('update.html', blogpost=blogpost)
    flash('You are not a valid user to Edit this Post')
    return redirect(url_for('show_posts'))

if __name__ == '__main__':
    blog.run()
