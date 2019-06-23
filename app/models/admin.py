from enum import IntEnum

from peewee import CharField, ForeignKeyField, SmallIntegerField

from app.extensions import db
from app.utils import enum2choices


class Role(db.Model):
    class Permission(IntEnum):
        READ = 1
        WRITE = 2
        DELETE = 4

    name = CharField(null=False)
    level = SmallIntegerField(choices=enum2choices(Permission))


class User(db.Model):
    role = ForeignKeyField(Role, Role.name, backref='users')
    username = CharField()
    password = CharField()
