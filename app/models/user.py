from flask_login import UserMixin
from .user_data import UserData


class User(UserMixin):
    def __init__(self, user_data: UserData) -> None:
        self.id = user_data.id
        self.username = user_data.username
        self.password = user_data.password
