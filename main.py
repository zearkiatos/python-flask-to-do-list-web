from flask import render_template, abort, redirect, url_for
from flask_login import login_required, current_user
from app import create_app
from app.firestore_service import get_todos
import unittest

app = create_app()

NOT_FOUND = 404
INTERNAL_SERVER_ERROR = 500


@app.route("/home", methods=['GET'])
@login_required
def home():
    try:
        user = current_user
        todos = get_todos(user.id)
        print(user)
        context = {
            "username": user.username,
            "todos": todos
        }
        print(user)

        return render_template('home.html', **context)
    except Exception:
        abort(INTERNAL_SERVER_ERROR)


@app.route("/")
def index():
    return redirect(url_for('auth.login'))


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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)
