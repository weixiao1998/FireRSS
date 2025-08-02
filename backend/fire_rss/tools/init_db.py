from sqlmodel import SQLModel

from fire_rss.base.db import engine
from fire_rss.models import *  # noqa


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    create_db_and_tables()
