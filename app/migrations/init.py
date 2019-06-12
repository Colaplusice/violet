from app.extensions import db
from app.models.user import Article, Author, Tag


def migrate_up():
    with db.database.atomic():
        db.database.create_tables([Article, Author, Tag])
        print("run successful!")


def rollback():
    pass
