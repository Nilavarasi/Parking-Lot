from functools import wraps
from flask import session


def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        print("entering in")
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            return
    return wrap
