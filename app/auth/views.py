from flask import render_template, session, redirect, flash, url_for
from . import auth
from flask_login import login_user, login_required, logout_user
from app.forms.LoginForm import LoginForm
from app.firestore_service import get_users, get_todos, get_user
from app.models.user_data import UserData
from app.models.user import User

INTERNAL_SERVER_ERROR = 500


@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    context = {
        'login_form': login_form
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data
        users = get_users()
        login_success = False
        for user in users:
            login_success = user.to_dict()['password'] == password and user.to_dict()['name'] == username
            if login_success:
                user_data = UserData(user.id, username=user.to_dict()['name'], password=user.to_dict()['password'])
                userFound = User(user_data)
                print(userFound)
                login_user(userFound)
                break
            # todos = get_todos(user.id)
        if login_success:
            flash('Welcome again')
            return redirect(url_for('home'))
        else:
            flash('The user does not exist')
        # user_context = {
        #     'user': userDict,
        #     'todos': todos,
        #     'username': username
        # }

    return render_template('login.html', **context)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Bye, bye, see you later")
    
    return redirect(url_for('auth.login'))

