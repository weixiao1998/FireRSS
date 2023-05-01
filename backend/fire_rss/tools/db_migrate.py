from os.path import dirname

import click


def _get_router():
    from fire_rss.base.db import db
    from fire_rss.base.log import logger
    from peewee_migrate import Router

    parent_dir = dirname(dirname(__file__))
    return Router(db, f"{parent_dir}/db_migrations", ignore="basemodel", logger=logger)


@click.group()
def cli():
    pass


@cli.command()
@click.argument("migration_name")
def create(migration_name):
    router = _get_router()
    router.create(migration_name, auto="fire_rss.models")


@cli.command()
def run():
    router = _get_router()
    router.run()


if __name__ == "__main__":
    cli()
