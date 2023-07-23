from flask import render_template, session, redirect, flash, url_for
from werkzeug.security import generate_password_hash
from . import auth
from flask_login import login_user, login_required, logout_user
from app.forms.LoginForm import LoginForm
from app.firestore_service import get_users, get_todos, get_user, get_user_by_username, post_user
from app.models.user_data import UserData
from app.models.new_user_data import NewUserData
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
            login_success = user.to_dict()['password'] == password and user.to_dict()[
                'name'] == username
            if login_success:
                user_data = UserData(user.id, username=user.to_dict()[
                                     'name'], password=user.to_dict()['password'])
                userFound = User(user_data)
                login_user(userFound)
                break
        if login_success:
            flash('Welcome again')
            return redirect(url_for('home'))
        else:
            flash('The user does not exist')

    return render_template('login.html', **context)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Bye, bye, see you later")

    return redirect(url_for('auth.login'))


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    signup_form = LoginForm()
    context = {
        'signup_form': signup_form
    }
    if signup_form.validate_on_submit():
        username = signup_form.username.data
        password = signup_form.password.data

        user_doc = get_user_by_username(username)

        if not user_doc:
            password_hash = generate_password_hash(password)
            new_user_data = NewUserData(username, password=password_hash)
            post_user(new_user_data)

            new_user = get_user_by_username(new_user_data.username)[0]

            login_user(UserData(
                id=new_user.id,
                username=new_user_data.username,
                password=new_user_data.password
            ))

            flash('Welcome!')

            return redirect(url_for('home'))
    else:
      flash('The user exists')

    return render_template('signup.html', **context)
