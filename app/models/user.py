import pendulum
from peewee import CharField, ForeignKeyField, TextField, DateTimeField

from app.extensions import db


class Author(db.Model):
    name = CharField(null=False, unique=True)


class Tag(db.Model):
    name = CharField(null=False, unique=True)


class Article(db.Model):
    author = ForeignKeyField(Author, Author.name)
    title = CharField(null=False)
    tag = ForeignKeyField(Tag, Tag.name)
    created_at = DateTimeField(default=pendulum.now(tz='utc'))
    content = TextField(null=False)
