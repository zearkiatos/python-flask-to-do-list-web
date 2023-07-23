import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore_v1.base_query import FieldFilter
from app.utils.path_resolver import get_project_root

credential = credentials.Certificate(str(get_project_root())+'/cert/cert.json')
firebase_admin.initialize_app(credential)

db = firestore.client()


def get_users():
    return db.collection('users').get()


def get_user(user_id):
    return db.collection('users').document(user_id).get()

def get_user_by_username(username):
    return db.collection('users').where(filter=FieldFilter("name", "==", username)).get()

def post_user(new_user_data):
    db.collection('users').add({
        "name": new_user_data.username,
        "password": new_user_data.password
    })

def get_todos(user_id):
    return db.collection('users').document(user_id).collection('todos').get()

def post_todo(user_id, description):
    todos_collection_ref = db.collection('users').document(user_id).collection('todos')
    todos_collection_ref.add({
        'description': description,
        'done': False
    })

def delete_todo(user_id, todo_id):
    todo_ref = _get_todo_ref(user_id, todo_id)
    todo_ref.delete()

def update_todo(user_id, todo_id, done):
    todo_ref = _get_todo_ref(user_id, todo_id)
    todo_ref.update({
        'done': not done
    })

def _get_todo_ref(user_id, todo_id):
    return db.document('users/{}/todos/{}'.format(user_id,todo_id))