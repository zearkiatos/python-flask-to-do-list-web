from flask import render_template, session, flash, redirect, url_for, abort
from app import create_app
from app.forms.LoginForm import LoginForm
import unittest

app = create_app()

NOT_FOUND = 404
INTERNAL_SERVER_ERROR = 500

@app.route("/")
def index():
    return "Hello World! 👋 🌎 Flask 🌶️"

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)
    pass

@app.errorhandler(NOT_FOUND)
def not_found(error):
    return render_template('404.html', error=error)


@app.errorhandler(INTERNAL_SERVER_ERROR)
def internal_server_error(error):
    return render_template('500.html', error=error)

@app.route("/login", methods=['GET', 'POST'])
def login():
    try:
        login_form = LoginForm()
        username = session.get('username')
        context = {
            'login_form': login_form,
            'username': username
        }

        if login_form.validate_on_submit():
            username = login_form.username.data
            session['username'] = username

            flash('User saved successful')
            return redirect(url_for('login'))

        return render_template("login.html", **context)
    except Exception:
        abort(INTERNAL_SERVER_ERROR)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)