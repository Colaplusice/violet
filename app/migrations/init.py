from app.extensions import db


def migrate_up():
    print("run successful!")
    db.database.create_tables([])


def rollback():
    pass
