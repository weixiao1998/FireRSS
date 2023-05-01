import bcrypt
from playhouse.shortcuts import model_to_dict

from ..base import const, errors
from ..base.db import db
from ..models.user import User


class UserManager:
    @staticmethod
    def format_user(user):
        if user and not isinstance(user, dict):
            return model_to_dict(user)
        return user

    @staticmethod
    def format_users(users):
        return [UserManager.format_user(u) for u in users]

    @db.atomic()
    def create_user(
        self,
        name,
        raw_password,
        status=const.UserStatus.PENDING,
        user_type=const.UserType.NORMAL,
    ):
        user = User.select().where(User.name == name).for_update().first()
        if user is not None:
            raise errors.UserExistsError
        if not isinstance(raw_password, bytes):
            raw_password = raw_password.encode()
        password = bcrypt.hashpw(raw_password, bcrypt.gensalt())
        user = User.create(name=name, password=password, status=status, type=user_type)
        return user

    def get_user_list(self, page_size, page_num, name=None):
        query = []
        if name:
            query.append(User.name.contains(name))
        users = list(User.select().where(*query if query else [None]))
        return users
