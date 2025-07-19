import bcrypt
from fastapi import Depends
from sqlmodel import select

from ..base import const, errors
from ..base.db import get_session
from ..models.user import User

dep_get_session = Depends(get_session)


class UserManager:
    @classmethod
    async def create_user(
        cls,
        name,
        raw_password,
        status=const.UserStatus.PENDING,
        user_type=const.UserType.NORMAL,
        session=dep_get_session,
    ):
        user = await session.exec(select(User).where(User.name == name))
        user = User.select().where(User.name == name).for_update().first()
        if user is not None:
            raise errors.UserExistsError
        if not isinstance(raw_password, bytes):
            raw_password = raw_password.encode()
        password = bcrypt.hashpw(raw_password, bcrypt.gensalt())
        user = User.create(name=name, password=password, status=status, type=user_type)
        return user

    @classmethod
    def get_user_list(cls, page_size, page_num, name=None):
        query = []
        if name:
            query.append(User.name.contains(name))
        users = list(User.select().where(*query if query else [None]))
        return users
