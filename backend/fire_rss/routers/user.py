from fastapi import APIRouter

import fire_rss.models as m
from fire_rss.base.db import SessionDep
from fire_rss.managers.user import UserManager

router = APIRouter(prefix="/api/v1/users")


@router.get("/")
async def get_user_list(
    session: SessionDep, name: str | None = None, page_size: int = 20, page_num: int = 1
) -> list[m.UserOut]:
    return UserManager(session).get_user_list(page_size, page_num, name=name)


@router.post("/sign_up")
async def user_sign_up(session: SessionDep, user: m.UserSignUp) -> m.UserOut:
    return UserManager(session).create_user(user.name, user.password)
