from flask import render_template
from . import main

@main.errorhandler(403)
def forbidden(e):
    error_title = "Forbidden"
    error_msg = "You shouldn't be here!"
    return render_template('error.html',
                           error_title=error_title,
                           error_msg=error_msg), 403


@main.errorhandler(404)
def page_not_found(e):
    error_title = "Not Found"
    error_msg = "That page doesn't exist"
    return render_template('error.html',
                           error_title=error_title,
                           error_msg=error_msg), 404


@main.errorhandler(500)
def internal_server_error(e):
    error_title = "Internal Server Error"
    error_msg = "Sorry, we seem to be experiencing some technical difficulties"
    return render_template('error.html',
                           error_title=error_title,
                           error_msg=error_msg), 500