from flask import render_template, session
from functools import wraps

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not "email" in session:
            return render_template('error/403.html'), 403
        return f(*args, **kwargs)
    return decorated
