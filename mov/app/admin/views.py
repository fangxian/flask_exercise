from . import admin
from functools import wraps
from flask import session, render_template, redirect, url_for, request
from ..models import User


def admin_login_req(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "admin" not in session:
            return redirect(url_for("admin.login"))
        return f(*args, **kwargs)

    return decorated_function


@admin.route("/")
@admin_login_req
def admin_index():
    return render_template("admin/index")


@admin.route("/login")
def admin_login():
    pass


@admin.route("/logout")
@admin_login_req
def admin_logout():
    pass


@admin.route("/edit_pwd")
def admin_edit_pwd():
    pass
