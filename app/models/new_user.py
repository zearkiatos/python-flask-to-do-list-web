from flask_login import UserMixin
from .new_user_data import NewUserData


class NewUser(UserMixin):
    def __init__(self, new_user_data: NewUserData) -> None:
        self.username = new_user_data.username
        self.password = new_user_data.password