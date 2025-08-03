from contextlib import contextmanager
from typing import Annotated

from fastapi import Depends
from sqlalchemy import create_engine
from sqlmodel import Session

from ..config import config

engine = create_engine(**config.DB_ENGINE_CONFIG)


def get_session():
    with Session(engine) as session:
        yield session


@contextmanager
def db_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
