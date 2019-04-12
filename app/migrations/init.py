from app.extensions import db
from app.models.user import Article, Author, Tag


def migrate_up():
    print("run successful!")
    db.database.create_tables([Article, Author, Tag])


def rollback():
    pass
