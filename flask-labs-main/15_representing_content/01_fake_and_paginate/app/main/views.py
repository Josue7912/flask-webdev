# -*- coding: utf-8 -*-

from flask import render_template, redirect, request, url_for, current_app
from werkzeug.exceptions import abort
from flask_login import current_user, login_required

from app.main import main
from app.main.forms import TodoForm, TodoListForm
from app.models import Todo, TodoList


@main.route("/")
def index():
    form = TodoForm()
    if form.validate_on_submit():
        return redirect(url_for("main.new_todolist"))
    return render_template("index.html", form=form)


@main.route("/todolists/", methods=["GET", "POST"])
@login_required
def todolist_overview():
    form = TodoListForm()
    if form.validate_on_submit():
        return redirect(url_for("main.add_todolist"))
    return render_template("overview.html", form=form)


def _get_user():
    return current_user.username if current_user.is_authenticated else None


@main.route("/todolist/<int:id>/", methods=["GET", "POST"])
def todolist(id):
    todolist = TodoList.query.filter_by(id=id).first_or_404()
    form = TodoForm()
    if form.validate_on_submit():
        Todo(form.todo.data, todolist.id, _get_user()).save()
        return redirect(url_for("main.todolist", id=id))
    page = request.args.get('page', 1, type=int)
    pagination = \
    Todo.query.filter_by(todolist=todolist).order_by(Todo.created_at.desc()).paginate(
        page,
        per_page=current_app.config['APP_TODOS_PER_PAGE'],
        error_out=False)
    todos = pagination.items
    return render_template("todolist.html", todolist=todolist, form=form, todos=todos, pagination=pagination)


@main.route("/todolist/new/", methods=["POST"])
def new_todolist():
    form = TodoForm(todo=request.form.get("todo"))
    if form.validate():
        todolist = TodoList(creator=_get_user()).save()
        Todo(form.todo.data, todolist.id).save()
        return redirect(url_for("main.todolist", id=todolist.id))
    return redirect(url_for("main.index"))


@main.route("/todolist/add/", methods=["POST"])
def add_todolist():
    form = TodoListForm(todo=request.form.get("title"))
    if form.validate():
        todolist = TodoList(form.title.data, _get_user()).save()
        return redirect(url_for("main.todolist", id=todolist.id))
    return redirect(url_for("main.index"))


@main.route("/todo/<int:todo_id>/", methods=["GET", "PUT"])
def update_todo_status(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    if request.method == "GET":
        return todo.to_dict()
    try:
        if request.json.get("is_finished"):
            todo.finished()
        else:
            todo.reopen()
    except:
        abort(400)
    return todo.to_dict()
