import datetime
from blog import db
from peewee import *


class Post(db.Model):
    id = PrimaryKeyField()
    name = CharField(index=True)
    text = TextField()
    created_date = DateTimeField(default=datetime.datetime.now)
    change_date = DateTimeField(null=False)

    def __repr__(self):
        return "<Post %r>" % self.name