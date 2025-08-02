import bcrypt
from sqlmodel import Session, select

from ..base import const, errors, utils
from ..models.user import User


class UserManager:
    def __init__(self, session):
        self.session: Session = session

    def create_user(
        self,
        name,
        raw_password,
        nick_name=None,
        status=const.UserStatus.PENDING,
        user_type=const.UserType.NORMAL,
    ):
        user = self.session.exec(select(User).where(User.name == name)).first()
        if user is not None:
            raise errors.UserExistsError
        if not isinstance(raw_password, bytes):
            raw_password = raw_password.encode()
        hashed_password = bcrypt.hashpw(raw_password, bcrypt.gensalt())
        user = User(
            name=name,
            hashed_password=hashed_password,
            status=status,
            type=user_type,
            nick_name=nick_name if nick_name else name,
            create_time=utils.utc_now(),
        )
        self.session.add(user)
        self.session.commit()
        return user

    def get_user_list(self, page_size, page_num, name=None):
        qs = select(User)
        query = []
        if name:
            query.append(User.name.contains(name))
        if query:
            qs = qs.where(*query)
        users = self.session.exec(qs).all()
        return users
