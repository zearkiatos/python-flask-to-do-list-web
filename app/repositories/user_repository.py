from ..firestore_service import get_user
from ..models.user_data import UserData
from ..models.user import User


class UserRepository:
    @staticmethod
    def find(user_id):
        user_doc = get_user(user_id)
        user = UserData(id=user_doc.id, username=user_doc.to_dict(
        )['name'], password=user_doc.to_dict()['password'])

        return User(user)
