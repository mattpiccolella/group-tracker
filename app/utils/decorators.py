from flask import render_template, redirect
from functools import wraps
from app.utils import is_authenticated

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not is_authenticated():
            return render_template('error/403.html'), 403
        return f(*args, **kwargs)
    return decorated

def redirect_for_no_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not is_authenticated():
            return redirect("/")
        return f(*args, **kwargs)
    return decorated
