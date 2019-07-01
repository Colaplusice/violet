from playhouse.migrate import SqliteMigrator, migrate

from app.extensions import db
from app.models.user import Article


def migrate_up():
    migrator = SqliteMigrator(db.database)
    migrate(
        migrator.add_column(
            Article._meta.table_name, Article.view_num.column_name, Article.view_num
        )
    )


def rollback():
    pass
