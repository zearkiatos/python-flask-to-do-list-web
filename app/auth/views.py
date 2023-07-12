from flask import render_template, session, redirect, flash, url_for
from . import auth
from app.forms.LoginForm import LoginForm

INTERNAL_SERVER_ERROR = 500


@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    context = {
        'login_form': login_form
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username
        flash('User saved successful')

        return redirect(url_for('auth.login'))

    return render_template('login.html', **context)
