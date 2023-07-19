from flask import render_template, session, redirect, flash, url_for
from . import auth
from app.forms.LoginForm import LoginForm
from app.firestore_service import get_users, get_todos

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
        users = get_users()
        for user in users:
            userDict = user.to_dict()
            todos = get_todos(user.id)
        user_context = {
            'user': userDict,
            'todos': todos,
            'username': username
        }

        flash('User saved successful')

        return render_template('home.html', **user_context)

    return render_template('login.html', **context)
