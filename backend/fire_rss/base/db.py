from peewee import Model
from playhouse.pool import PooledMySQLDatabase

from ..config import config

if config.DB_CONFIG["db_type"] == "mysql":
    db = PooledMySQLDatabase("fire_rss", **config.DB_CONFIG["args"])
else:
    raise NotImplementedError


class BaseModel(Model):
    """base model for peewee"""

    class Meta:
        database = db


def init_peewee(app):
    @app.teardown_request
    def close_db(exc):
        if not db.is_closed():
            db.close()
