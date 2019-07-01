from playhouse.migrate import SqliteMigrator, migrate

from app.extensions import db


def migrate_up():
    migrator = SqliteMigrator(db.database)
    migrate(migrator.rename_column('article', 'author_id', 'author_name'))
    migrate(migrator.rename_column('article', 'tag_id', 'tag_name'))


def rollback():
    pass
