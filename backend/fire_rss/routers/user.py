from fastapi import APIRouter

from ..managers.user import UserManager

router = APIRouter(prefix="/api/v1/users")


@router.get("/")
async def get_user_list(name: str | None = None, page_size: int = 20, page_num: int = 1):
    return UserManager.get_user_list(page_size, page_num, name=name)
