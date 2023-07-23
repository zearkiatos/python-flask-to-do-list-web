from flask import url_for, redirect
from . import todos
from flask_login import current_user
from app.firestore_service import delete_todo, update_todo

INTERNAL_SERVER_ERROR = 500

@todos.route('/delete/<todo_id>', methods=['POST'])
def delete(todo_id):
    user_id = current_user.id
    delete_todo(user_id, todo_id)

    return redirect(url_for('home'))

@todos.route('/update/<todo_id>/<int:done>', methods=['POST'])
def update(todo_id, done):
    user_id = current_user.id

    update_todo(user_id, todo_id, done)

    return redirect(url_for('home'))
