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


def get_todos(user_id):
    return db.collection('users').document(user_id).collection('todos').get()


def get_user(user_id):
    return db.collection('users').document(user_id).get()

def get_user_by_username(username):
    return db.collection('users').where(filter=FieldFilter("name", "==", username)).get()

def post_user(new_user_data):
    db.collection('users').add({
        "name": new_user_data.username,
        "password": new_user_data.password
    })
