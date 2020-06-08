from functools import wraps

from flask import current_app as app, request, session, redirect, url_for, flash, render_template
from flask_login import login_required, logout_user, login_user

from src.infrastructure.injector import user_signup, get_user_with_credentials


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect((url_for('login')))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user = get_user_with_credentials.execute(request.form['username'],
                                                 request.form['password'])
        if not user:
            error = 'Invalid Credentials. Please try again.'
            return render_template('login.html', error=error), 401
        login_user(user)
        return redirect(url_for('shopping'))
    return render_template('login.html', error=error)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = None
    if request.method == 'POST':
        user_info = {
            'username': request.form['username'],
            'password': request.form['password']
        }
        new_user = user_signup.execute(user_info)
        login_user(new_user)
        return redirect(url_for('shopping'))
    return render_template('signup.html', error=error)


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('/login'))

    return wrap
