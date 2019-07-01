from datetime import datetime

from peewee import CharField, ForeignKeyField, TextField, DateTimeField, IntegerField

from app.extensions import db


class Author(db.Model):
    name = CharField(null=False, unique=True)


class Tag(db.Model):
    name = CharField(null=False, unique=True)


class Article(db.Model):
    author = ForeignKeyField(Author, Author.name, column_name='author_name', backref='articles')
    title = CharField(null=False, unique=True)
    tag = ForeignKeyField(Tag, Tag.name, column_name='tag_name', backref='articles')
    created_at = DateTimeField(default=datetime.now())
    content = TextField(null=False)
    view_num = IntegerField(default=0)
