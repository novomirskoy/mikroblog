from flask import Flask
from flask_peewee.db import Database
from peewee import *


app = Flask(__name__)
app.config.from_object("config")
app.config['DATABASE'] = {
	"name": "blog.db",
	"engine": "peewee.SqliteDatabase",
}
db = Database(app)

from blog import views
from blog import forms
from blog import models

models.Post.create_table(fail_silently=True)