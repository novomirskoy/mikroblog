import datetime
from blog import db
from peewee import *


class Post(db.Model):
    id = PrimaryKeyField()
    name = CharField(index=True, null=False)
    text = TextField(null=False)
    created_date = DateTimeField(default=datetime.datetime.now)
    change_date = DateTimeField(null=True)

    def __repr__(self):
        return "<Post %r>" % self.name