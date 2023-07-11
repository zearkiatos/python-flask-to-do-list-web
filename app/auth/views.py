from flask import render_template
from . import auth
from app.forms.LoginForm import LoginForm

INTERNAL_SERVER_ERROR = 500


@auth.route('/login')
def login():
    context = {
        'login_form': LoginForm()
    }
    return render_template('login.html', **context)
