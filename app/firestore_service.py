import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
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
